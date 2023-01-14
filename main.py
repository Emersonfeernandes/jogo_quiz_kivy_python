import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from model import Pergunta, session
from sqlalchemy import select
from my_widgets import Acertou, Errou, Game_over
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.image import Image
from sound_ import sound1, sound2, doido, ensino, perdendo
from kivy.config import Config

Config.read("rungame.ini")

class Dancando(Image):
    def __init__(self, **kwargs):
        super(Dancando, self).__init__(**kwargs)
        Clock.schedule_once(self.update)

        self.list_dancando = ['dancando0', 'dancando1.zip',
            'dancando2.zip', 'dancando3.zip', 'dancando4.zip',
            'dancando5.zip', 'dancando6.zip']

    def update(self, *args):
        var = random.choice(self.list_dancando)
        self.source=f'ima_game/{var}'
        self.size_hint=(.3,.3) 
        self.pos_hint={'center_x':.7, 'center_y':.2}
        self.allow_stretch = True
        self.anim_delay = 0.1
        self.anim_loop =3
        #self.texture_size=(350,496)

class Principal(ScreenManager):
    pass


class My_Game(Screen):
    def __init__(self, **kwargs):
        super(My_Game, self).__init__(**kwargs)
        Clock.schedule_once(self.comecar)
    
        self.lista_principal = []
        
        self.cal = object
        self.certo = 0
        self.errado = 0

        self.true = False
        
        self.cor = Animation()

        self.valor = True
        statement = select(Pergunta.pergunta, Pergunta.opicoes, Pergunta.resposta)

        result = session.execute(statement).all()
        random.shuffle(result)

        for t in result:    
            lista = list(t)
            self.lista_principal.append(lista)
        #print(len(self.lista_principal))
        

    def comecar(self, *args):
        self.ids.acertos.text = f'Acertos: {self.certo}'
        self.ids.erros.text = f'Erros: {self.errado}'
        
        if not self.lista_principal:
            ga = Game_over()
            ga.fim(self.certo, self.errado)
            pop = Popup(title='', separator_height=0, content=ga, size_hint=(.6,0.5))
            title_ = pop.children[0].children[2]
            title_.height = 0
            pop.open()

        if self.valor == True:
            for self.i in self.lista_principal:
                self.ids.pergun.text = f'{self.i[0]}'

                opi_id = 'opi'
                n = 0
                s = self.i[1]

                for op in s.split('\n'):
                    strin = str(n)
                    x = opi_id + strin
                    
                    self.ids[f'{x}'].text = f'{op}'
                    n +=1
                self.valor = False
                n = 0
                break
        if self.valor == True:
            pass
            
                

    def responder(self, txt):
        self.ima = Dancando()
        if txt == self.i[2]:
            sound1.play()
            del self.lista_principal[0]
            self.certo += 1
            print('acertou')
            op = 'opi'
            n = 0
            self.true = True
            for i in range(3):
                strin = str(n)
                x = op + strin
                if txt == self.ids[f'{x}'].text:
                    self.cor = Animation(background_color=(0,1,0,1), duration=0.2) + Animation(background_color=(0,0,1,1), duration=0.2)
                    self.var_id = self.ids[f'{x}']
                    self.cor.repeat = True
                    self.cor.start(self.var_id)
                    break
                    #self.ids[f'{x}'].background_color = (0,1,0)
                    
                n+=1
            n = 0
            self.ids.perguntasss.add_widget(self.ima)
            self.cal = Acertou()
            telinha = Animation(size_hint=(0.37, 0.29), duration=0.2, t='in_bounce')
            telinha.start(self.cal)
            
            self.ids.perguntasss.add_widget(self.cal)
            Clock.schedule_once(self.novamente, 3)
            
        else:
            sound2.play()
            del self.lista_principal[0]
            self.errado += 1
            op = 'opi'
            n = 0
            for i in range(3):
                strin = str(n)
                x = op + strin
                if txt == self.ids[f'{x}'].text:
                    self.ids[f'{x}'].background_color = (1,0,0)
                if self.ids[f'{x}'].text == self.i[2]:
                    self.ids[f'{x}'].background_color = (0,1,0)

                n+=1
            n =0
            
            self.cal = Errou()
            telinha = Animation(size_hint=(0.37, 0.29), duration=0.2, t='in_bounce')
            telinha.start(self.cal)
            self.ids.perguntasss.add_widget(self.cal)

            Clock.schedule_once(self.novamente, 3)

    def novamente(self, *args):
        if self.true == True:
            self.cor.stop(self.var_id)
            self.true = False
            self.ids.perguntasss.remove_widget(self.ima)

        if self.certo == 10 and self.errado == 0:
            ensino.play()
        if self.certo == 20 and self.errado == 0:
            doido.play()
        if self.certo == 0 and self.errado == 2:
            perdendo.play()
        op = 'opi'
        n = 0
        for i in range(3):
            strin = str(n)
            x = op + strin
            self.ids[f'{x}'].background_color = (0,0,1)
            n+=1
        n =0
        self.ids.perguntasss.remove_widget(self.cal)
        self.valor = True
        Clock.schedule_once(self.comecar)

        

class Vamos_Comecar(Screen):
    def __init__(self, **kwargs):
        super(Vamos_Comecar, self).__init__(**kwargs)
        Clock.schedule_once(self.image)

    def image(self, *args):
        self.ima = Image(source='ima_game/Ciência-Cérebro-PNG.png', size_hint=(.3,.3), pos_hint={'center_x':.5, 'center_y':.2})
        self.ids.inicio.add_widget(self.ima)
        
    def inicio(self):
        anim1 = Animation(size_hint=(.02,.02), pos_hint={'center_y':.9}, font_size=5)
        anim = Animation(size_hint=(.6,.6), pos_hint={'center_y':.4})
        anim1.start(self.ids.btn_comecar)
        anim.start(self.ima)
        game = My_Game()
        game.valor = True
        Clock.schedule_once(self.primeira_pergunta, 1.5)

    def primeira_pergunta(self, *args):
        self.parent.current = 'my_game'



class RunGame(App):
    def build_config(self, config):
        config.setdefaults('postproc', {
            'retain_time': '3000',
            'retain_distance': '3000'
        })
        
    def build(self):
        return Builder.load_file("RunGame.kv")
    


if __name__ == '__main__':
    RunGame().run()