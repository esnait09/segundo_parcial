import pygame
from objects import Object
from os import listdir
from os.path import isfile, join

class Block(Object):
    """
    Representa un bloque del terreno en el juego.

    Hereda de la clase `Object` y añade funcionalidad para cargar y gestionar diferentes tipos de bloques de terreno.

    Atributos:
    image (pygame.Surface): Imagen que representa el bloque.
    mask (pygame.mask.Mask): Máscara de colisión para el bloque.
    """

    def __init__(self, x, y, size, terrain):
        """
        Inicializa un bloque en una posición específica con un tamaño y tipo de terreno dado.

        Parámetros:
        x (int): Coordenada x del bloque.
        y (int): Coordenada y del bloque.
        size (int): Tamaño del bloque (ancho y alto).
        terrain (str): Tipo de terreno del bloque (e.g., "terrain1", "terrain2", "terrain3").
        """
        super().__init__(x, y, size, size)
        block = self.get_block(size, terrain)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def get_block(self, size, terrain):
        """
        Carga la imagen del bloque del terreno y crea una superficie transparente con el tipo de terreno especificado.

        Parámetros:
        size (int): Tamaño del bloque (ancho y alto).
        terrain (str): Tipo de terreno del bloque.

        Retorna:
        pygame.Surface: Superficie con la imagen del bloque escalada.
        """
        path = join("src", "assets", "Terrain", "Terrain.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)

        # Define la región de la imagen que corresponde al tipo de terreno
        if terrain == "terrain1":
            rect = pygame.Rect(96, 70, size, size)
        elif terrain == "terrain2":
            rect = pygame.Rect(96, 70, size, size)
        elif terrain == "terrain3":
            rect = pygame.Rect(96, 70, size, size)
        else:
            # En caso de un tipo de terreno no reconocido, usa una región predeterminada
            rect = pygame.Rect(0, 0, size, size)

        # Crea y escala la superficie del bloque
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)
