import pandas as pd
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import InstructionGroup, Color, Rectangle
from kivy.uix.image import Image
from io import BytesIO

class PieChartApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Button to load data and generate the pie chart
        load_button = Button(text='Load Pie Chart')
        load_button.bind(on_release=self.load_data_and_plot)

        self.chart_image = Image()

        layout.add_widget(load_button)
        layout.add_widget(self.chart_image)

        return layout

    def load_data_and_plot(self, instance):
        # Load the data from the CSV file
        data = pd.read_csv('daily_activity_data.csv')

        # Ensure 'from_time' and 'to_time' columns are in datetime format
        data['from_time'] = pd.to_datetime(data['from_time'])
        data['to_time'] = pd.to_datetime(data['to_time'])

        # Calculate time spent on each activity
        data['time_spent'] = (data['to_time'] - data['from_time']).dt.total_seconds() / 3600  # Convert seconds to hours

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

if __name__ == '__main__':
    PieChartApp().run()