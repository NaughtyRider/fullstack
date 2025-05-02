import logging
import sqlite3
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivymd.app import MDApp
from kivymd.uix.pickers import *#MDTimePicker,MDModalDatePicker
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
import pandas as pd
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import InstructionGroup, Color, Rectangle
from kivy.uix.image import Image
from io import BytesIO
logging.basicConfig(level=logging.WARNING) #to suppress debug
logging.basicConfig(level=logging.WARNING)

# Suppress Kivy-specific logging
kivy_logger = logging.getLogger('kivy')
kivy_logger.setLevel(logging.WARNING)

# Suppress Matplotlib-specific logging
matplotlib_logger = logging.getLogger('matplotlib')
matplotlib_logger.setLevel(logging.WARNING)
class DateClass(MDApp):
    def __init__(self,add_detail, **kwargs):
        super().__init__(**kwargs)
        self.add_detail=add_detail
    def build(self):
        self.time=None
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        print('-------------------Hello-------------')
        # return MDTimePicker().time
        return (
            MDScreen(
                MDRaisedButton(
                    text="Open time picker",
                    pos_hint={'center_x': .5, 'center_y': .5},
                    on_release=self.show_date_picker,
                )
            )
        )
    
    def show_date_picker(self, *args):
        date_dialog = MDDatePicker()
        date_dialog.theme_cls.theme_style = "Dark"
        date_dialog.theme_cls.primary_palette = "Orange"
        date_dialog.bind(on_save=self.get_date)
        date_dialog.open()

    def get_date(self, instance, value,date_range):
        print("---------------Date---------")
        # print(self.add_detail.text)
        self.add_detail.text=str(value)
        # print(time)

class DailyGraph(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        # self.button_layout = BoxLayout(orientation='horizontal')
        self.button_layout = GridLayout(cols=4, row_default_height=40, row_force_default=True,size_hint_y=0.1)
        self.table = GridLayout(cols=6, row_default_height=40, row_force_default=True,size_hint_y=None)
        self.table.bind(minimum_height=self.table.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1,0.9), size=(400, 300))

        back_button = Button(text='Go Back')
        back_button.bind(on_press=self.go_back)
        self.button_layout.add_widget(back_button)
        back_button = Label()
        self.button_layout.add_widget(back_button)
        back_button = Label()
        self.button_layout.add_widget(back_button)
        back_button = Button(text='logout')
        back_button.bind(on_press=self.logout)
        self.button_layout.add_widget(back_button)
        self.date = Button(
            text="Select Date",
            halign='center',
            height=10,
            size_hint=(0.3,0.1 ),
            pos_hint={'center_x': 0.5},
            on_release=lambda x: DateClass(self.date).show_date_picker()
            )
        
        self.button_layout.add_widget(self.date)
        refresh_button = Button(text='Refresh Data')
        refresh_button.bind(on_press=self.load_data_and_plot)
        self.button_layout.add_widget(refresh_button)

        # layout.add_widget(self.date)
        
        self.chart_image = Image()
        

        self.layout.add_widget(self.button_layout)
        self.layout.add_widget(self.chart_image)
        # print('In sel/f')
        # Adding headers

        # Adding a button to simulate adding a new row (optional)

        self.add_widget(self.layout)
        
        
   
    def go_back(self, instance):
        self.manager.current = 'review'  
    def logout(self, instance):
        self.manager.current = 'login'
    def add_row(self, instance):
        # This method can be expanded to actually add a new row
        self.manager.current = 'add'
    
    
    def update_row(self, row_id):

        database = 'entries'
        table = 'valuess'
        conn = sqlite3.connect(f'{database}.db')
        c = conn.cursor()
        
        from_value = self.from_input.text
        to_value = self.to_input.text
        activity_value = self.activity_input.text
        
        c.execute(f"UPDATE {table} SET date = ?, to_time = ?, activity = ? WHERE id = ?",
                  (from_value, to_value, activity_value, row_id))
        conn.commit()
        conn.close()
        self.popup.dismiss()
        self.refresh_data()  # Refresh the data after update

    def load_data_and_plot(self,instance):
        # Load the data from the CSV file
        data = pd.read_csv('screens/daily_activity_data.csv')
        print("------------------------------------------")
        print(len(data))
        print(self.date.text)
        if self.date !='Select Date':
            data=data[data['date'].astype(str)==str(self.date.text)]
            print(len(data))

        else:
            print(len(data))
            data=data[data['date'].astype(str)=='2025-02-17']
            print(len(data))
        print(data.index)
        print(data.columns)
        print(data.head(1))

        # Ensure 'from_time' and 'to_time' columns are in datetime format
        data['from_time'] = pd.to_datetime(data['from_time'])
        data['to_time'] = pd.to_datetime(data['to_time'])

        # Calculate time spent on each activity
        data['time_spent'] = abs((data['to_time'] - data['from_time']).dt.total_seconds() / 3600)  # Convert seconds to hours

        # Sum the time spent on each activity
        activity_time_spent = data.groupby('activity')['time_spent'].sum()

        # Create a pie chart
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(activity_time_spent, labels=activity_time_spent.index, 
               autopct=lambda pct: self.func(pct, activity_time_spent), startangle=140)
        ax.set_title('Daily Activities Time Distribution')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Save the plot to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)  # Close the figure to free up memory
        buf.seek(0)

        # Convert to Kivy texture
        texture = self.get_texture_from_image(buf)

        # Update the image widget with the new texture
        self.chart_image.texture = texture

    def get_texture_from_image(self, buf):
        from kivy.graphics.texture import Texture
        from PIL import Image as PILImage

        image = PILImage.open(buf)
        image = image.transpose(PILImage.FLIP_TOP_BOTTOM)  # Flip the image

        texture = Texture.create(size=image.size)
        texture.blit_buffer(image.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
        return texture

    def func(self, pct, allvalues):
        total = sum(allvalues)
        absolute = int(pct / 100. * total)
        hours = absolute
        return f'{hours}h\n({pct:.1f}%)'
