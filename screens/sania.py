from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HelloSaniaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Hello Sania!", font_size=50)
        layout.add_widget(label)

        back_button = Button(text="Back to Hello World", font_size=30)
        back_button.bind(on_press=self.go_to_world)  # Use a method
        layout.add_widget(back_button)

        logout_button = Button(text="Logout", font_size=30)  # Logout button
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)

        self.add_widget(layout)

    def go_to_world(self, instance):
        self.manager.current = 'world'

    def logout(self, instance):
        self.manager.current = 'login'