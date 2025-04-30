
import logging
import kivy
from kivy.app import App
from kivy.uix.screenmanager import * #ScreenManager,SlideTransition,WipeTransition
import sqlite3
for logger in logging.Logger.manager.loggerDict:
    logging.getLogger(logger).setLevel(logging.WARNING)
logging.basicConfig(level=logging.WARNING)

# Suppress Kivy-specific logging
kivy_logger = logging.getLogger('kivy')
kivy_logger.setLevel(logging.WARNING)

# Suppress Matplotlib-specific logging
matplotlib_logger = logging.getLogger('matplotlib')
matplotlib_logger.setLevel(logging.WARNING)
kivy.require('2.0.0')
# Import your screens
from screens.login import LoginScreen
from screens.mainfile import First
from screens.hello import HelloWorldScreen
from screens.sania import HelloSaniaScreen
from screens.add_screen import Add_detail
from screens.update_record import Update_record
from screens.Review import Review
from screens.daily_graph import DailyGraph

def init_db():
    database='entries'
    table='valuess'
    conn = sqlite3.connect(f'{database}.db')
    c = conn.cursor()
    # c.execute('drop table valuess')
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT,from_time TEXT,to_time TEXT,activity TEXT,category TEXT)''')
    conn.commit()
    table_list = [a for a in c.execute(f"SELECT name FROM sqlite_master WHERE type = 'table' ")]
        # here is you table list
    print(table_list)
    c.execute(f"SELECT * FROM {table} ")
    data=c.fetchall()
        # here is you table list
    print(data)
    conn.close()
init_db()

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=WipeTransition()) #to change screen transition can use also FallOutTransition()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(First(name='main'))
        sm.add_widget(Add_detail(name='add'))
        sm.add_widget(Review(name='review'))
        sm.add_widget(DailyGraph(name='Graph'))
        sm.add_widget(Update_record(name='Update_record'))
        sm.add_widget(HelloWorldScreen(name='world1'))
        sm.add_widget(HelloSaniaScreen(name='sania'))
        sm.current = 'review'
        return sm

if __name__ == '__main__':
    MyApp().run()
