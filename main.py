from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("photo library.kv")


class QuizPageApp(App):
    def build(self):
        return PhotoManager()
class PhotoManager(ScreenManager):
    pass

class PhotoLibrary(Screen):
    pass