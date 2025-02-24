from turtle import right
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class First(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ... (HelloWorldScreen code - same as before)

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

        button = Button(text="Add", font_size=30)
        button.bind(on_press=self.go_to_add)  # Use a method
        # child2.add_widget(button)
        layout.add_widget(button)
        self.add_hover_effect(button)

        button = Button(text="Review", font_size=30)
        button.bind(on_press=self.go_to_review)  # Use a method
        # child2.add_widget(button)
        layout.add_widget(button)
        self.add_hover_effect(button)

        # logout_button = Button(text="Logout", font_size=30)
        # logout_button.bind(on_press=self.logout)
        # layout.add_widget(logout_button)

        # self.add_widget(layout)
        # self.add_hover_effect(button)
        self.add_widget(layout)
        
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