import sqlite3
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class Review(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        # self.button_layout = BoxLayout(orientation='horizontal')
        self.button_layout = GridLayout(cols=2, row_default_height=40, row_force_default=True,size_hint_y=0.1)
        self.table = GridLayout(cols=4, row_default_height=40, row_force_default=True,size_hint_y=None)
        self.table.bind(minimum_height=self.table.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1,0.9), size=(400, 300))

        add_button = Button(text='Add Row')
        add_button.bind(on_press=self.add_row)
        self.button_layout.add_widget(add_button)
        refresh_button = Button(text='Refresh Data')
        refresh_button.bind(on_press=self.refresh_data)
        self.button_layout.add_widget(refresh_button)
        self.button_layout.add_widget(Label())

        self.scroll_view.add_widget(self.table)

        self.layout.add_widget(self.button_layout)
        self.layout.add_widget(self.scroll_view)
        print('In Review')
        # Adding headers

        # Adding a button to simulate adding a new row (optional)

        self.add_widget(self.layout)
    def on_pre_enter(self):
        self.refresh_data()
        
        
    def refresh_data(self,instance=None):
        self.table.clear_widgets()
        headers = ['id','From', 'To', 'Activity']
        for header in headers:
            self.table.add_widget(Label(text=header, bold=True))
        database='entries'
        table='valuess'
        conn = sqlite3.connect(f'{database}.db')
        c = conn.cursor()
        
        c.execute(f"SELECT * FROM {table} ")
        self.data=c.fetchall()
        # here is you table list
        data=self.data
        print(data)
        
        conn.close() 
        # Sample data


        # Adding data rows
        for row in data:
            for item in row:
                self.table.add_widget(Label(text=str(item)))
        
        
    def add_row(self, instance):
        # This method can be expanded to actually add a new row
        self.manager.current = 'add'