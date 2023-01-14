from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from model import Pergunta, session

Builder.load_file("mais_.kv")

class CadastrarPergunta(FloatLayout):
    
    def on_text(self, value):      
        if self.ids.fazer_pergunta.text != '' and self.ids.opcoes_resposta.text != '' and self.ids.resposta_certa.text != '':
            self.ids.salve.disabled = False
        if value == '':
            self.ids.salve.disabled = True
            

    def salvar(self):
        
        desp = Pergunta(
            pergunta = self.ids.fazer_pergunta.text,
            opicoes = self.ids.opcoes_resposta.text,
            resposta = self.ids.resposta_certa.text,
        )

        session.add(desp)

        session.commit()

        self.ids.fazer_pergunta.text = ''
        self.ids.opcoes_resposta.text = ''
        self.ids.resposta_certa.text = ''       

class Add_Pergunta(App):
    def build(self):
        return CadastrarPergunta()

if __name__ == '__main__':
    Add_Pergunta().run()