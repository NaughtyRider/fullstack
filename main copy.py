# from tkinter import font
# from kivy.app import App
# from kivy.uix.scatter import Scatter
# from kivy.uix.label import Label
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.gridlayout import GridLayout
# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.uix.pickers import MDTimePicker
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.screen import MDScreen
# from numpy import size
# import random
# class ShowScatter(BoxLayout):
#     def change_label_color(self,*args):
#         color  =  [random.random() for i in range(3)] +[1]
#         label = self.ids['my_label']
#         label.color = color
# class MyApp(App):
#     def build(self):
#         return ShowScatter()
       
# def some(*args):
#     print('text changed')
# KV = '''
# MDFloatLayout:

#     MDRaisedButton:
#         text: "Open time picker"
#         pos_hint: {'center_x': .5, 'center_y': .5}
#         on_release: app.show_time_picker()
# '''
# class Test(MDApp):
    
#     def build(self):
#         self.time=None
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Orange"
#         print('-------------------Hello-------------')
#         # return MDTimePicker().time
#         return (
#             MDScreen(
#                 MDRaisedButton(
#                     text="Open time picker",
#                     pos_hint={'center_x': .5, 'center_y': .5},
#                     on_release=self.show_time_picker,
#                 )
#             )
#         )

#     def show_time_picker(self, *args):
#         time_dialog = MDTimePicker()
#         time_dialog.bind(time=self.get_time)
#         time_dialog.open()

#     def get_time(self, instance, time):
#         '''
#         The method returns the set time.

#         :type instance: <kivymd.uix.picker.MDTimePicker object>
#         :type time: <class 'datetime.time'>
#         '''
#         print("---------------Time---------")
#         # print(time)
#         self.time=time
#         print(self.time)
#         # return time
# if __name__ == '__main__':
#     Test().run()

# import kivy
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivymd.app import MDApp
# from kivymd.uix.button import MDFlatButton
# from kivymd.uix.pickers import MDDatePicker
# import sqlite3

# kivy.require('2.0.0')

# # Database setup
# def init_db():
#     conn = sqlite3.connect('entries.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS entries (name TEXT, age INTEGER, from_date TEXT, to_date TEXT)''')
#     conn.commit()
#     conn.close()

# class EntryForm(BoxLayout):
#     def __init__(self, **kwargs):
#         super(EntryForm, self).__init__(**kwargs)
#         self.orientation = 'vertical'

#         # Name input
#         self.add_widget(Label(text='Name:'))
#         self.name_input = TextInput(multiline=False)
#         self.add_widget(self.name_input)

#         # Age input
#         self.add_widget(Label(text='Age:'))
#         self.age_input = TextInput(multiline=False)
#         self.add_widget(self.age_input)

#         # From date input
#         self.add_widget(Label(text='From Date:'))
#         self.from_date_input = TextInput(multiline=False, readonly=True)
#         self.from_date_input.bind(on_focus=self.open_date_picker_from)
#         self.add_widget(self.from_date_input)

#         # To date input
#         self.add_widget(Label(text='To Date:'))
#         self.to_date_input = TextInput(multiline=False, readonly=True)
#         self.to_date_input.bind(on_focus=self.open_date_picker_to)
#         self.add_widget(self.to_date_input)

#         # Submit button
#         self.submit_button = MDFlatButton(text='Submit')
#         self.submit_button.bind(on_press=self.submit)
#         self.add_widget(self.submit_button)

#     def open_date_picker_from(self, instance, value):
#         if value:
#             date_dialog = MDDatePicker(callback=self.set_from_date)
#             date_dialog.open()

#     def open_date_picker_to(self, instance, value):
#         if value:
#             date_dialog = MDDatePicker(callback=self.set_to_date)
#             date_dialog.open()

#     def set_from_date(self, date):
#         self.from_date_input.text = date.strftime("%Y-%m-%d")

#     def set_to_date(self, date):
#         self.to_date_input.text = date.strftime("%Y-%m-%d")

#     def submit(self, instance):
#         name = self.name_input.text
#         age = self.age_input.text
#         from_date = self.from_date_input.text
#         to_date = self.to_date_input.text
        
#         if name and age.isdigit() and from_date and to_date:
#             self.save_to_db(name, int(age), from_date, to_date)
#             self.name_input.text = ''
#             self.age_input.text = ''
#             self.from_date_input.text = ''
#             self.to_date_input.text = ''

#     def save_to_db(self, name, age, from_date, to_date):
#         conn = sqlite3.connect('entries.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO entries (name, age, from_date, to_date) VALUES (?, ?, ?, ?)", 
#                   (name, age, from_date, to_date))
#         conn.commit()
#         conn.close()

# class MyApp(MDApp):
#     def build(self):
#         init_db()
#         return EntryForm()

# if __name__ == '__main__':
#     MyApp().run()
from turtle import onclick
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivymd.uix.pickers import MDDatePicker
import sqlite3

kivy.require('2.0.0')

# Database setup
def init_db():
    conn = sqlite3.connect('entries.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries (name TEXT, age INTEGER, from_date TEXT, to_date TEXT)''')
    conn.commit()
    conn.close()

class EntryForm(BoxLayout):
    def __init__(self, **kwargs):
        super(EntryForm, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Name input
        self.add_widget(Label(text='Name:'))
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        # Age input
        self.add_widget(Label(text='Age:'))
        self.age_input = TextInput(multiline=False)
        self.add_widget(self.age_input)

        # From date input
        self.add_widget(Label(text='From Date:'))
        self.from_date_input = Button(text='From')
        self.from_date_input.bind(on_release=self.open_date_picker_from)
        self.add_widget(self.from_date_input)

        # To date input
        self.add_widget(Label(text='To Date:'))
        self.to_date_input = Button(text='To')
        self.to_date_input.bind(on_focus=self.open_date_picker_to)
        self.add_widget(self.to_date_input)

        # Submit button
        self.submit_button = MDFlatButton(text='Submit')
        self.submit_button.bind(on_press=self.submit)
        self.add_widget(self.submit_button)

    def open_date_picker_from(self,*args):
        if True:
            date_dialog = MDDatePicker(callback=self.set_from_date)
            date_dialog.open()

    def open_date_picker_to(self, instance):
        if True:
            date_dialog = MDDatePicker(callback=self.set_to_date)
            date_dialog.open()

    def set_from_date(self, date):
        self.from_date_input.text = date.strftime("%Y-%m-%d")

    def set_to_date(self, date):
        self.to_date_input.text = date.strftime("%Y-%m-%d")

    def submit(self, instance):
        name = self.name_input.text
        age = self.age_input.text
        from_date = self.from_date_input.text
        to_date = self.to_date_input.text
        
        if name and age.isdigit() and from_date and to_date:
            self.save_to_db(name, int(age), from_date, to_date)
            self.name_input.text = ''
            self.age_input.text = ''
            self.from_date_input.text = ''
            self.to_date_input.text = ''

    def save_to_db(self, name, age, from_date, to_date):
        conn = sqlite3.connect('entries.db')
        c = conn.cursor()
        c.execute("INSERT INTO entries (name, age, from_date, to_date) VALUES (?, ?, ?, ?)", 
                  (name, age, from_date, to_date))
        conn.commit()
        conn.close()

class MyApp(MDApp):
    def build(self):
        init_db()
        return EntryForm()

if __name__ == '__main__':
    MyApp().run()