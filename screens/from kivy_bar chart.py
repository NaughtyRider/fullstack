from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg as FigureCanvas
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

def fetch_data_from_db(date):
    # Connect to the SQLite database
    con = sqlite3.connect('daily_activity.db')  # Replace with your database file
    query = f"SELECT date, from_time, to_time, activity FROM activities where date='{date}'"
    df = pd.read_sql_query(query, con)
    con.close()

    # Convert from_time and to_time to datetime
    df['from_time'] = pd.to_datetime(df['from_time'], format='%H:%M:%S')
    df['to_time'] = pd.to_datetime(df['to_time'], format='%H:%M:%S')

    # Calculate time spent in minutes
    df['time_spent'] = (df['to_time'] - df['from_time']).dt.total_seconds() / 60

    # Group by activity and sum time spent
    activity_time = df.groupby('activity')['time_spent'].sum().reset_index()
    return activity_time

class ChartApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Show Total Time Spent on Activities')
        button.bind(on_press=self.show_chart)
        layout.add_widget(button)
        return layout

    def show_chart(self, instance):
        # Fetch data from the database
        df = fetch_data_from_db('2025-02-04')

        # Create a bar chart for total time spent
        plt.figure(figsize=(10, 6))
        plt.bar(df['activity'], df['time_spent']//60, color='skyblue')
        plt.title('Total Time Spent on Daily Activities')
        plt.xlabel('Activity')
        plt.ylabel('Total Time Spent (hours)')
        plt.xticks()
        plt.grid(axis='y', linestyle='--')

        # Add the chart to the Kivy layout
        self.canvas = FigureCanvas(plt.gcf())
        self.root.add_widget(self.canvas)

if __name__ == '__main__':
    ChartApp().run()