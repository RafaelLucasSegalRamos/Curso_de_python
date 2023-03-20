import pygame
import os
from random import shuffle

while True:
    try:

        music_path = "C:/xampp/htdocs/Curso_de_python/Aula_08-Utilizando_Modulos/EX/musica"

        music_list = os.listdir(music_path)
        # song = AudioSegment.from_mp3("nightcore_circus.mp3")
        # play(song)

        music_folder = 'musica'
        os.chdir(music_folder)
        shuffle(music_list)
        for musica in music_list:
            pygame.mixer.init()
            pygame.mixer.music.load(musica)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        os.chdir('../')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
