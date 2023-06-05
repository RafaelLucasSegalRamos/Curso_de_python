import pygame
import os
from random import shuffle

try:
    music_path = "musica/"

    music_list = os.listdir(music_path)
    shuffle(music_list)

    pygame.mixer.init()
    for musica in music_list:
        filename = os.path.join(music_path, musica)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

except KeyboardInterrupt:
    print('\033[91m\nO usuário parou o programa\033[0m')

except ValueError:
    print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

except:
    print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
