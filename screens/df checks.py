from datetime import datetime
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        
        to_time = Button(text='Select Category', size_hint=(None, None), size=(200, 50))
        layout.add_widget(to_time)
        # Create a dropdown
        dropdown = DropDown()

        # Define the categories
        categories = ['Education', 'Self-Care', 'Work', 'Exercise', 'Leisure','Waste']

        # Create buttons for each category and add them to the dropdown
        for category in categories:
            btn = Button(text=category, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        # Create a main button that will open the dropdown
        self.main_button = Button(text='Select Category', size_hint=(None, None), size=(200, 50))
        self.main_button.bind(on_release=dropdown.open)

        # Bind the selected category to the main button's text
        dropdown.bind(on_select=lambda instance, x: setattr(self.main_button, 'text', x))

        # Add the button to the layout
        layout.add_widget(self.main_button)
        print(datetime.today().date())

        return layout

if __name__ == '__main__':
    MyApp().run()