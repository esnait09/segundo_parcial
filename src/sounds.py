import pygame 

pygame.mixer.init()

background_music = pygame.mixer.music.load('./src/assets/sounds/music2.mp3')
laser_sound = pygame.mixer.Sound('./src/assets/sounds/shot.wav')
coin_sound = pygame.mixer.Sound('./src/assets/sounds/coin.mp3')
game_over_sound = pygame.mixer.Sound('./src/assets/sounds/game_over.mp3')
win_sound = pygame.mixer.Sound('./src/assets/sounds/win.mp3')
         