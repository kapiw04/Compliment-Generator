import random
import string

from kivy import utils
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from platformdirs.windows import Windows

templates = [
    'Your %slowo1%n %be %slowo2',
    'You have %a%n%slowo2 %slowo1'
]

rz = open("rzeczowniki2.txt", "r", encoding='utf8')
word_one = rz.read().splitlines()
pl = open("plural.txt", "r", encoding='utf8')
plural = pl.read().splitlines()
for i in plural:
    word_one.append(i)
pr = open("przymiotniki.txt", "r", encoding='utf8')
word_two = pr.read().splitlines()

Window.size = (414, 896)


class Cgenerator(BoxLayout):
    c = StringProperty('')

    def random_c(self):
        _one = random.choice(word_one).lower()
        _two = random.choice(word_two).lower()
        self.c = random.choice(templates).replace('%slowo1', _one)
        self.c = self.c.replace('%slowo2', _two)
        if _one in plural:
            self.c = self.c.replace('%a', '')
            self.c = self.c.replace('%be', 'are')
        elif _two.startswith(('a', 'e', 'i', 'o', 'u', 'y')):
            self.c = self.c.replace('%a', 'an ')
            self.c = self.c.replace('%be', 'is')
        else:
            self.c = self.c.replace('%a', 'a ')
            self.c = self.c.replace('%be', 'is')
        if len(self.c) > 30:
            self.c = self.c.replace('%n', '\n')
        else:
            self.c = self.c.replace('%n', '')


class Cgen(App):
    pass


Cgen().run()
