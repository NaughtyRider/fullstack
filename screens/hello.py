from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HelloWorldScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ... (HelloWorldScreen code - same as before)

        layout = BoxLayout(orientation='vertical')

        label = Label(text="Hello World!", font_size=50)
        layout.add_widget(label)

        button = Button(text="Go to Hello Sania Screen", font_size=30)
        button.bind(on_press=self.go_to_sania)  # Use a method
        layout.add_widget(button)

        logout_button = Button(text="Logout", font_size=30)
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)

        self.add_widget(layout)

    def go_to_sania(self, instance):
        self.manager.current = 'sania'

    def logout(self, instance):
        self.manager.current = 'login'