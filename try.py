import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('2.0.0')

class SimpleButtonsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        button1 = Button(text="Button 1")  # Basic button
        layout.add_widget(button1)

        button2 = Button(text="Button 2", size_hint=(0.5, None), height=50)  # Size hint and height
        layout.add_widget(button2)

        button3 = Button(text="Button 3", size_hint=(None, None), size=(100, 40))  # Fixed size
        layout.add_widget(button3)
        
        return layout

# if __name__ == '__main__':
    # SimpleButtonsApp().run()

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('2.0.0')

class SideBySideButtonsApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', padding=20, spacing=10)  # Horizontal layout

        button1 = Button(text="Button 1",size_hint=(0.5, None), height=50)
        layout.add_widget(button1)

        button2 = Button(text="Button 2")
        layout.add_widget(button2)

        return layout

if __name__ == '__main__':
    SideBySideButtonsApp().run()