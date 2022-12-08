from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):

        return Builder.load_file('my.kv')


if __name__ == '__main__':
    MyApp().run()