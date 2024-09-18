import pygame
from constants import *

class Button:
<<<<<<< HEAD
    """
    Representa un botón interactivo en la interfaz gráfica.

    Atributos:
    text (str): Texto que se muestra en el botón.
    x (int): Coordenada x del botón.
    y (int): Coordenada y del botón.
    width (int): Ancho del botón.
    height (int): Altura del botón.
    color (tuple): Color del botón cuando no está en estado hover.
    hover_color (tuple): Color del botón cuando el ratón está sobre él.
    action (callable): Acción a ejecutar cuando el botón es presionado (por defecto None).
    rect (pygame.Rect): Rectángulo que define la posición y tamaño del botón.
    hovered (bool): Estado del botón, si el ratón está sobre él.
    """

    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        """
        Inicializa un botón.

        Parámetros:
        text (str): Texto que se muestra en el botón.
        x (int): Coordenada x del botón.
        y (int): Coordenada y del botón.
        width (int): Ancho del botón.
        height (int): Altura del botón.
        color (tuple): Color del botón cuando no está en estado hover.
        hover_color (tuple): Color del botón cuando el ratón está sobre él.
        action (callable): Acción a ejecutar cuando el botón es presionado (por defecto None).
        """
=======
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.rect = pygame.Rect(x, y, width, height)
        self.hovered = False

    def draw(self, win):
<<<<<<< HEAD
        """
        Dibuja el botón en la ventana.

        Parámetros:
        win (pygame.Surface): La superficie (ventana) donde se dibuja el botón.
        """
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
        pygame.draw.rect(win, self.hover_color if self.hovered else self.color, self.rect, border_radius=5)
        font = pygame.font.SysFont("Poppins", 25)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        win.blit(text, text_rect)

    def is_hovered(self, pos):
<<<<<<< HEAD
        """
        Verifica si el ratón está sobre el botón.

        Parámetros:
        pos (tuple): Coordenadas del ratón (x, y).

        """
        self.hovered = self.rect.collidepoint(pos)
        
class ToggleButton(Button):
    """
    Representa un botón que alterna entre dos estados.

    Atributos:
    text1 (str): Texto del primer estado del botón.
    text2 (str): Texto del segundo estado del botón.
    color1 (tuple): Color del botón en el primer estado.
    color2 (tuple): Color del botón en el segundo estado.
    action1 (callable): Acción a ejecutar en el primer estado.
    action2 (callable): Acción a ejecutar en el segundo estado.
    """

    def __init__(self, text1, text2, x, y, width, height, color1, color2, action1, action2):
        """
        Inicializa un botón que alterna entre dos estados.

        Parámetros:
        text1 (str): Texto del primer estado del botón.
        text2 (str): Texto del segundo estado del botón.
        x (int): Coordenada x del botón.
        y (int): Coordenada y del botón.
        width (int): Ancho del botón.
        height (int): Altura del botón.
        color1 (tuple): Color del botón en el primer estado.
        color2 (tuple): Color del botón en el segundo estado.
        action1 (callable): Acción a ejecutar en el primer estado.
        action2 (callable): Acción a ejecutar en el segundo estado.
        """
=======
        self.hovered = self.rect.collidepoint(pos)
        
class ToggleButton(Button):
    def __init__(self, text1, text2, x, y, width, height, color1, color2, action1, action2):
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
        super().__init__(text1, x, y, width, height, color1, color2, action1)
        self.text1 = text1
        self.text2 = text2
        self.action1 = action1
        self.action2 = action2

    def toggle(self):
<<<<<<< HEAD
        """
        Alterna entre los dos estados del botón.
        Cambia el texto y la acción del botón según su estado actual.
        """
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
        if self.text == self.text1:
            self.text = self.text2
            self.action = self.action2
        else:
            self.text = self.text1
<<<<<<< HEAD
            self.action = self.action1
=======
            self.action = self.action1
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
