import pygame

class Object(pygame.sprite.Sprite):
    """
    Crea un objeto en el juego que es un sprite básico.
    Hereda de pygame.sprite.Sprite para integrarse con el sistema de sprites de Pygame.
    """
    
    def __init__(self, x, y, width, height, name=None):
        """
        Inicializa el objeto con posición, tamaño y un nombre opcional.
        
        Parámetros:
        x (int): Coordenada x en la pantalla.
        y (int): Coordenada y en la pantalla.
        width (int): Ancho del objeto.
        height (int): Altura del objeto.
        name (str, opcional): Nombre del objeto. Por defecto es None.
        """
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        
    def draw(self, win):
        """
        Dibuja el objeto en la ventana del juego.
        
        Parámetros:
        win (pygame.Surface): La superficie (ventana) donde se dibujará el objeto.
        """
        win.blit(self.image, (self.rect.x, self.rect.y))
