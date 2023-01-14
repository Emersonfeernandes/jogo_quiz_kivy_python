from kivy.core.audio import SoundLoader
from kivy.uix.image import Image

sound1 = SoundLoader.load('sound_game/ACERTOU.mp3')

sound2 = SoundLoader.load('sound_game/ERROU.mp3')

doido = SoundLoader.load('sound_game/doido.mp3')

ensino = SoundLoader.load('sound_game/quem_ensinou.mp3')

perdendo = SoundLoader.load('sound_game/perdendo.mp3')

ima2 = Image(source='ima_game/dancando.png.zip', 
            size_hint=(.3,.3), pos_hint={'center_x':.6, 'center_y':.2},
            allow_stretch = True, anim_delay = 0.1, anim_loop =3, texture_size=(350,496))