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
        self.button_layout = GridLayout(cols=2, row_default_height=40, row_force_default=True)
        self.table = GridLayout(cols=4, row_default_height=40, row_force_default=True, size_hint_y=None)
        self.table.bind(minimum_height=self.table.setter('height'))  # Bind height for scrolling
        
        self.scroll_view = ScrollView(size_hint=(1, None), size=(400, 300))
        self.scroll_view.add_widget(self.table)

        add_button = Button(text='Add Row')
        add_button.bind(on_press=self.add_row)
        self.button_layout.add_widget(add_button)

        refresh_button = Button(text='Refresh Data')
        refresh_button.bind(on_press=self.refresh_data)
        self.button_layout.add_widget(refresh_button)
        self.button_layout.add_widget(Label())

        self.layout.add_widget(self.button_layout)
        self.layout.add_widget(self.scroll_view)

        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.refresh_data()

    def refresh_data(self, instance=None):
        self.table.clear_widgets()
        headers = ['id', 'From', 'To', 'Activity']
        for header in headers:
            self.table.add_widget(Label(text=header, bold=True))
        
        database = 'entries'
        table = 'valuess'
        conn = sqlite3.connect(f'{database}.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM {table}")
        self.data = c.fetchall()
        conn.close()
        
        # Adding data rows
        for row in self.data:
            for item in row:
                self.table.add_widget(Label(text=str(item)))

    def add_row(self, instance):
        # This method can be expanded to actually add a new row
        self.manager.current = 'add'

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem


Builder.load_string(
    '''
#:import images_path kivymd.images_path


<CustomOneLineIconListItem>

    IconLeftWidget:
        icon: root.icon


<PreviousMDIcons>

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDBoxLayout:
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: root.set_list_md_icons(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
)


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(Screen):

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()


MainApp().run()