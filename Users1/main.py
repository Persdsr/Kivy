from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout

from post_db import register

class Container(FloatLayout):
    def auth(self):
        register(self.login.text, self.password1.text, self.password2.text)
        print('акк зареган')


class MyApp(MDApp):
    def build(self):

        return Container()


if __name__ == '__main__':
    MyApp().run()
