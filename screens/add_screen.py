
import sqlite3
from turtle import right
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen

class Test(MDApp):
    def __init__(self,add_detail, **kwargs):
        super().__init__(**kwargs)
        self.add_detail=add_detail
    def build(self):
        self.time=None
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        print('-------------------Hello-------------')
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
        time_dialog.theme_cls.theme_style = "Dark"
        time_dialog.theme_cls.primary_palette = "Orange"
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        print("---------------Time---------")
        # print(self.add_detail.text)
        self.add_detail.text=str(time)
        # print(time)

class Add_detail(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        # child1 = BoxLayout(orientation='horizontal')
        # child2 = BoxLayout(orientation='vertical')
        # layout.add_widget(child1)
        # layout.add_widget(child2)

        logout_button = Button(text="Logout", font_size=20,size_hint=(0.1,0.1),pos_hint ={'center_x':.9})
        logout_button.bind(on_press=self.logout)
        logout_button.bind(font_size=logout_button.setter(self.width))
        # child1.add_widget(logout_button)
        layout.add_widget(logout_button)
        self.add_hover_effect(logout_button)
        label = Label(text="Welcome Nakul!", font_size=50)
        # child1.add_widget(label)
        layout.add_widget(label)
        
        # self.from_time = TextInput(hint_text="From",  halign='center',height=10,multiline=False,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        # self.from_time = Button(text="From",  halign='center',height=10,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        # self.from_time.bind(on_focus=self.open_date_picker_from)
        # # self.add_widget(self.from_date_input)
        # layout.add_widget(self.from_time)

        # self.to_time = TextInput(hint_text="To", halign='center',height=10,multiline=False,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        # self.to_time = Button(text="To", halign='center',height=10,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        # self.to_time = Label(text='Select time',halign='center',
        #     height=10,
        #     size_hint=(0.3,0.1 ),
        #     pos_hint={'center_x': 0.5})
        self.from_time = Button(
            text="Select From Time",
            halign='center',
            height=10,
            size_hint=(0.3,0.1 ),
            pos_hint={'center_x': 0.5},
            on_release=lambda x: Test(self.from_time).show_time_picker()
            )
        
        layout.add_widget(self.from_time)
        
        self.to_time = Button(
            text="Select To Time",
            halign='center',
            height=10,
            size_hint=(0.3,0.1 ),
            pos_hint={'center_x': 0.5},
            on_release=lambda x: Test(self.to_time).show_time_picker()
            )
        
        layout.add_widget(self.to_time)
        # layout.add_widget(self.timebuttom)

        self.Activity = TextInput(hint_text="Activity",  halign='center',height=10,multiline=False,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        layout.add_widget(self.Activity)

        # self.to_time = TextInput(hint_text="Group", halign='center',height=10,multiline=False,size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        # layout.add_widget(self.to_time)

        add_button = Button(text="Click to Add!",  size_hint=(0.3,0.1 ),pos_hint={'center_x': 0.5})
        add_button.bind(on_press=self.add_detail)
        layout.add_widget(add_button)


        # logout_button = Button(text="Logout", font_size=30)
        # logout_button.bind(on_press=self.logout)
        # layout.add_widget(logout_button)

        # self.add_widget(layout)
        # self.add_hover_effect(button)
        self.add_widget(layout)


    

    
    
    # def set_to_time(self,time):
    #     self.to_time=time

        
    def add_detail(self, instance):
        from_time = self.from_time.text
        to_time = self.to_time.text
        Activity = self.Activity.text
        # password = self.password_input.text

        # if username == "admin" and password == "admin":  # Check credentials (INSECURE - use hashing in real app)
        # if username == "admin" and password == "admin":  # Check credentials (INSECURE - use hashing in real app)
        # if username == "admin" and password == "admin":  # Check credentials (INSECURE - use hashing in real app)
        if from_time and to_time and Activity:
            self.save_to_db(from_time, to_time, Activity)
            self.from_time.text = ''
            self.to_time.text = ''
            self.Activity.text = ''
            # self.to_date_input.text = ''
        print('------------------------------------------------------')
        # print(self.from_time.text, self.to_time.text, self.Activity.text)
        self.from_time.text=""  # Go to Hello World screen
        self.to_time.text = ""  # Clear input fields
        self.Activity.text = ""
        self.manager.current = 'main'
        # else:
        #     popup = Popup(title='Error', content=Label(text='Invalid credentials'), size_hint=(None, None), size=(200, 100))
        #     popup.open()
    def save_to_db(self, from_time , to_time, Activity):
        database='entries'
        table='valuess'
        conn = sqlite3.connect(f'{database}.db')
        c = conn.cursor()
        c.execute(f"INSERT INTO {table} (from_time, to_time, activity) VALUES (?, ?, ?)", 
                  (from_time , to_time, Activity))
        conn.commit()
        c.execute(f"SELECT * FROM {table} ")
        data=c.fetchall()
        # here is you table list
        print(data)
        conn.close()   
    def add_hover_effect(self,button):
        def on_enter(instance):
            instance.background_color = (0,0,1,1)
        def on_leave(instance):
            instance.background_color = (1,1,1,1)
        button.bind(on_enter=on_enter)
        button.bind(on_leave=on_leave)
        

    def go_to_add(self, instance):
        self.manager.current = 'add'
    def go_to_review(self, instance):
        self.manager.current = 'review'
    def logout(self, instance):
        self.manager.current = 'login'
