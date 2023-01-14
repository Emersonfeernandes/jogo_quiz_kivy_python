from kivy.uix.button import Label
from kivy.uix.button import Button
from  kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class BOTAO(Button):
     pass

class LABEL(Label):
    pass

class Acertou(BoxLayout):
    pass

class Errou(BoxLayout):
    pass

class Game_over(BoxLayout):
    def fim(self, txt, txt1):
        self.ids.fim.text = f'Você acertou {txt} e errou {txt1}!'


Builder.load_file("mais_.kv")