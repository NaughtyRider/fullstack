from tkinter import font
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
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
if __name__ == '__main__':
    MyApp().run()