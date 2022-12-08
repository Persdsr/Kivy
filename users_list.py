from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarListItem, ILeftBody
from kivymd.uix.label import MDLabel

from kivy.lang import Builder
import sqlite3

KV = '''
<MyItemList>:

    LeftLabel:
        id: left_label

BoxLayout:

    ScrollView:

        MDList:
            id: scroll
'''


class MyItemList(OneLineAvatarListItem):
    '''Custom list item.'''


class LeftLabel(ILeftBody, MDLabel):
    '''Custom left container.'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        db = sqlite3.connect('Users.sqlite3')
        cur = db.cursor()
        cur.execute('SELECT login FROM users')
        items = cur.fetchall()
        print(items[0][0])
        for i in range(len(items[0])):
            item = MyItemList(text=str(items[0][i]))
            # print(item.ids)
            item.ids.left_label.text = str(i)

            self.root.ids.scroll.add_widget(item)




MainApp().run()