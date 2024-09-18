import pygame

class Coin(pygame.sprite.Sprite):
    """
    Representa una moneda en el juego que cae bajo la influencia de la gravedad.

    Atributos:
    GRAVITY (int): La constante de gravedad que afecta a la moneda.
    image (pygame.Surface): La imagen que representa la moneda.
    rect (pygame.Rect): El rectángulo que define la posición y tamaño de la moneda.
    y_vel (int): La velocidad vertical actual de la moneda.
    """

    GRAVITY = 1  

    def __init__(self, x, y):
        """
        Inicializa una moneda en una posición específica.

        Parámetros:
        x (int): Coordenada x de la moneda.
        y (int): Coordenada y de la moneda.
        """
        super().__init__()
        self.image = pygame.image.load("./src/assets/Consumible/bolsa_de_dinero.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_vel = 0  

    def update(self, platforms):
        """
        Actualiza la posición de la moneda, aplicando la gravedad y verificando colisiones con plataformas.

        Parámetros:
        platforms (pygame.sprite.Group): Un grupo de plataformas con las que la moneda puede colisionar.
        """
        self.y_vel += self.GRAVITY  
        self.rect.y += self.y_vel  

       
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                self.rect.bottom = platform.rect.top  
                self.y_vel = 0  
