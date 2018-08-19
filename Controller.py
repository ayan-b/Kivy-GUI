from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition

import add

class MainScreen(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("Controller.kv")

class Controller(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    Controller().run()