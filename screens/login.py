from re import MULTILINE
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

        title_label = Label(text="Login to See!", font_size=40)
        layout.add_widget(title_label)

        self.username_input = TextInput(hint_text="Username",  halign='center',height=10,multiline=False,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        layout.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Password", password=True, halign='center',height=10,multiline=False,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        layout.add_widget(self.password_input)

        login_button = Button(text="Login",  size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if username == "admin" and password == "admin":  # Check credentials (INSECURE - use hashing in real app)
            self.manager.current = 'main'  # Go to Hello World screen
            self.username_input.text = ""  # Clear input fields
            self.password_input.text = ""
        else:
            popup = Popup(title='Error', content=Label(text='Invalid credentials'), size_hint=(None, None), size=(200, 100))
            popup.open()