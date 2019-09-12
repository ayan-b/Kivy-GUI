from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
Window.fullscreen = True

import add

class MainScreen(Screen):
    def open_popup(self, reading):
        the_popup = Popup(title='Reading', content = Label(text=str(reading)), 
                      size_hint=(0.5, 0.5), size=(200, 200))
        the_popup.open()

class ScreenTwo(Screen):
    def open_popup(self, reading):
        the_popup = Popup(title='Reading', content = Label(text=str(reading)), 
                      size_hint=(0.5, 0.5), size=(200, 200))
        the_popup.open()

class ScreenManagement(ScreenManager):
    pass


Builder.load_file("Controller.kv")
presentation = ScreenManager()
presentation.add_widget(MainScreen())
presentation.add_widget(ScreenTwo())


class ControllerApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    ControllerApp().run()