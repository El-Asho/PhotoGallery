from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from PIL import Image
from os import name

Builder.load_file("PhotoEditor.kv")


class PhotoEditorApp(App):
    def build(self):
        return PhotoLibrary()


class PhotoLibrary(Screen):
    def invert(self, image):
        pass
    def sepia(self, image):
        image = Image.open(image)
        pixels = image.load()
        for h in range(image.size[1]):
            for w in range(image.size[0]):
                red = int((pixels[w, h][0] * .393 + pixels[w, h][1] * 0.769 + pixels[w, h][2] * 0.189))
                green = int((pixels[w, h][0] * .349 + pixels[w, h][1] * 0.686 + pixels[w, h][2] * 0.168))
                blue = int((pixels[w, h][0] * .272 + pixels[w, h][1] * 0.534 + pixels[w, h][2] * 0.131))
                pixels[w, h] = (red, green, blue)
if __name__ == "__main__":
    PhotoEditorApp().run()
