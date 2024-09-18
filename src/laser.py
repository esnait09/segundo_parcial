<<<<<<< HEAD

=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
import pygame
from constants import *

class Laser(pygame.sprite.Sprite):
<<<<<<< HEAD
    """
    Representa un láser en el juego.

    Atributos:
    x_vel -- Velocidad del láser, determinada por la dirección.
    direction -- Dirección en la que se mueve el láser ("right" o "left").
    image -- Imagen del láser.
    rect -- Rectángulo que define la posición y tamaño del láser.

    Métodos:
    __init__(self, x, y, width, height, direction) -- Inicializa el láser con posición, tamaño y dirección.
    update(self) -- Actualiza la posición del láser y verifica si se ha salido de la pantalla.
    draw(self, win) -- Dibuja el láser en la ventana del juego.
    """

    def __init__(self, x, y, width, height, direction):
        """
        Inicializa el láser con posición, tamaño y dirección.

        x -- Coordenada x inicial del láser.
        y -- Coordenada y inicial del láser.
        width -- Ancho del láser.
        height -- Altura del láser.
        direction -- Dirección en la que se mueve el láser ("right" o "left").
        """
=======
    def __init__(self, x, y, width, height, direction):
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 8 if direction == "right" else -8  # Velocidad del láser
        self.direction = direction
        self.image = pygame.image.load('./src/assets/Laser/bullet3.png')  # Carga la imagen del láser
<<<<<<< HEAD
        self.image = pygame.transform.scale(self.image, (100, 100))

    def update(self):
        """
        Actualiza la posición del láser y verifica si se ha salido de la pantalla.
        Si el láser está fuera de la pantalla, se elimina del grupo de sprites.
        """
=======
        self.image = pygame.transform.scale(self.image, (100,100))

    def update(self):
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
        self.rect.x += self.x_vel

        # Verifica si el láser se ha salido de la pantalla
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

    def draw(self, win):
<<<<<<< HEAD
        """
        Dibuja el láser en la ventana del juego.

        win -- La ventana donde se debe dibujar el láser.
        """
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
        win.blit(self.image, self.rect)
        