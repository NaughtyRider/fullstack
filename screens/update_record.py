from datetime import datetime
import sqlite3
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class Update_record(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        # self.button_layout = BoxLayout(orientation='horizontal')
        self.button_layout = GridLayout(cols=4, row_default_height=40, row_force_default=True,size_hint_y=0.1)
        self.table = GridLayout(cols=6, row_default_height=40, row_force_default=True,size_hint_y=None)
        self.table.bind(minimum_height=self.table.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1,0.9), size=(400, 300))

        back_button = Button(text='Go Back')
        back_button.bind(on_press=self.go_back)
        self.button_layout.add_widget(back_button)
        back_button = Label()
        self.button_layout.add_widget(back_button)
        back_button = Label()
        self.button_layout.add_widget(back_button)
        back_button = Button(text='logout')
        back_button.bind(on_press=self.logout)
        self.button_layout.add_widget(back_button)
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
        print('In Update_record')
        # Adding headers

        # Adding a button to simulate adding a new row (optional)

        self.add_widget(self.layout)
    def on_pre_enter(self):
        self.refresh_data()
        
        
    def refresh_data(self, instance=None,date=str(datetime.today().date())):
        self.table.clear_widgets()
        headers = ['ID', 'From', 'To', 'Activity', 'Update', 'Delete']
        for header in headers:
            self.table.add_widget(Label(text=header, bold=True))
        
        database = 'entries'
        table = 'valuess'
        conn = sqlite3.connect(f'{database}.db')
        c = conn.cursor()
        if str(self.date.text).replace(' ','').lower() =='selectdate':
            c.execute(f"SELECT * FROM {table} where date = {date}")
        else:
            c.execute(f"SELECT * FROM {table} where date = {self.date}")

        self.data = c.fetchall()
        conn.close()
        
        # Adding data rows
        for row in self.data:
            for item in row:
                self.table.add_widget(Label(text=str(item)))
            # Add buttons for update and delete
            update_button = Button(text='Update', size_hint_y=None, height=40)
            update_button.bind(on_press=lambda instance, row_id=row[0],from_time=row[1],to_time=row[2],activity=row[3]: self.show_update_popup(row_id,from_time,to_time,activity))
            delete_button = Button(text='Delete', size_hint_y=None, height=40)
            delete_button.bind(on_press=lambda instance, row_id=row[0]: self.confirm_delete(row_id))
            self.table.add_widget(update_button)
            self.table.add_widget(delete_button)
        
    def go_back(self, instance):
        self.manager.current = 'review'  
    def logout(self, instance):
        self.manager.current = 'login'
    def add_row(self, instance):
        # This method can be expanded to actually add a new row
        self.manager.current = 'add'
    def confirm_delete(self, row_id):
        # Show confirmation popup
        confirmation_popup = Popup(title='Confirm Deletion',
                                    content=Label(text=f'Are you sure you want to delete row ID {row_id}?'),
                                    size_hint=(0.8, 0.4))
        yes_button = Button(text='Yes')
        yes_button.bind(on_press=lambda instance: self.delete_row(row_id, confirmation_popup))
        no_button = Button(text='No')
        no_button.bind(on_press=confirmation_popup.dismiss)
        
        button_layout = BoxLayout(orientation='horizontal')
        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)
        
        confirmation_popup.content = BoxLayout(orientation='vertical')
        confirmation_popup.content.add_widget(Label(text=f'Are you sure you want to delete row ID {row_id}?'))
        confirmation_popup.content.add_widget(button_layout)
        
        confirmation_popup.open()
    def delete_row(self, row_id, popup):
        database = 'entries'
        table = 'valuess'
        conn = sqlite3.connect(f'{database}.db')
        c = conn.cursor()
        c.execute(f"DELETE FROM {table} WHERE id = ?", (row_id,))
        conn.commit()
        conn.close()
        popup.dismiss()  # Close the confirmation popup
        self.refresh_data()  # Refresh the data after deletion

    def show_update_popup(self, row_id,from_time,to_time,activity):
        self.popup = Popup(title=f'Update Row {row_id}', size_hint=(0.8, 0.5))
        layout = BoxLayout(orientation='vertical')
        
        self.id_input = TextInput(hint_text='ID (unchanged)', text=str(row_id), readonly=True)
        self.from_input = TextInput(hint_text='From', text=str(from_time),)
        self.to_input = TextInput(hint_text='To', text=str(to_time),)
        self.activity_input = TextInput(hint_text='Activity', text=str(activity),)
        
        update_button = Button(text='Update')
        update_button.bind(on_press=lambda instance: self.update_row(row_id))
        
        layout.add_widget(self.id_input)
        layout.add_widget(self.from_input)
        layout.add_widget(self.to_input)
        layout.add_widget(self.activity_input)
        layout.add_widget(update_button)
        
        self.popup.content = layout
        self.popup.open()

    def update_row(self, row_id):
        database = 'entries'
        table = 'valuess'
        conn = sqlite3.connect(f'{database}.db')
        c = conn.cursor()
        
        from_value = self.from_input.text
        to_value = self.to_input.text
        activity_value = self.activity_input.text
        
        c.execute(f"UPDATE {table} SET from_time = ?, to_time = ?, activity = ? WHERE id = ?",
                  (from_value, to_value, activity_value, row_id))
        conn.commit()
        conn.close()
        self.popup.dismiss()
        self.refresh_data()  # Refresh the data after update