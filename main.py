
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

kivy.require('2.0.0')

# Import your screens
from screens.login import LoginScreen
from screens.mainfile import First
from screens.hello import HelloWorldScreen
from screens.sania import HelloSaniaScreen
from screens.add_screen import Add_detail

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(First(name='main'))
        sm.add_widget(Add_detail(name='add'))
        sm.add_widget(HelloWorldScreen(name='world1'))
        sm.add_widget(HelloSaniaScreen(name='sania'))
        sm.current = 'main'
        return sm

if __name__ == '__main__':
    MyApp().run()
