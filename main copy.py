from tkinter import font
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from numpy import size
import random
class ShowScatter(BoxLayout):
    def change_label_color(self,*args):
        color  =  [random.random() for i in range(3)] +[1]
        label = self.ids['my_label']
        label.color = color
class MyApp(App):
    def build(self):
        return ShowScatter()
       
def some(*args):
    print('text changed')
KV = '''
MDFloatLayout:

    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
'''
class Test(MDApp):
    
    def build(self):
        self.time=None
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        print('-------------------Hello-------------')
        print(MDTimePicker().time)
        # return MDTimePicker().time
        return (
            MDScreen(
                MDRaisedButton(
                    text="Open time picker",
                    pos_hint={'center_x': .5, 'center_y': .5},
                    on_release=self.show_time_picker,
                )
            )
        )

    def show_time_picker(self, *args):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        '''
        The method returns the set time.

        :type instance: <kivymd.uix.picker.MDTimePicker object>
        :type time: <class 'datetime.time'>
        '''
        print("---------------Time---------")
        # print(time)
        self.time=time
        print(self.time)
        # return time
if __name__ == '__main__':
    MyApp().run()