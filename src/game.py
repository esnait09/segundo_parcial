import pygame 
from constants import *
from player import *
from laser import *
from objects import *
from enemies import *
from button import *
from coins import *
from menus import main_menu
from sounds import *



pygame.init()
pygame.mixer.init()
pygame.display.set_caption("ardal")
pygame.display.set_icon(pygame.image.load("./src/assets/Background/inicio_de_inicio.jpg"))

font = pygame.font.SysFont("Minecraft", 30)
window = pygame.display.set_mode((WIDTH, HEIGHT))
        
main_menu(window)