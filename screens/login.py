from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ... (LoginScreen code - same as before)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        title_label = Label(text="Login", font_size=40)
        layout.add_widget(title_label)

        self.username_input = TextInput(hint_text="Username", size_hint_y=None, height=40)
        layout.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Password", password=True, size_hint_y=None, height=40)
        layout.add_widget(self.password_input)

        login_button = Button(text="Login", size_hint_y=None, height=40)
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if username == "admin" and password == "admin":  # Check credentials (INSECURE - use hashing in real app)
            self.manager.current = 'world'  # Go to Hello World screen
            self.username_input.text = ""  # Clear input fields
            self.password_input.text = ""
        else:
            popup = Popup(title='Error', content=Label(text='Invalid credentials'), size_hint=(None, None), size=(200, 100))
            popup.open()