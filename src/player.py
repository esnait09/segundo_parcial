import pygame
from coins import Coin
from laser import Laser
from os import listdir
from os.path import isfile, join
from constants import *
from boss import Boss

class Player(pygame.sprite.Sprite):
    """Controla el funcionamiento del sprite del jugador en el juego."""
    COLOR = (255, 0, 0)
    GRAVITY = 1
    ANIMATION_DELAY = 4
    
    def __init__(self, x, y, width, height):
        """
        Inicializa una nueva instancia del jugador.

        Args:
            x (int): La posición horizontal inicial del jugador.
            y (int): La posición vertical inicial del jugador.
            width (int): El ancho del sprite del jugador.
            height (int): La altura del sprite del jugador.
        """
        
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.sprites = self.load_sprite_sheets("Characters", "player", 48, 48, True)
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.lives = 3
        self.invulnerable = False
        self.invulnerable_time = 0
        self.hit = False
        self.hit_count = 0
        self.lasers = pygame.sprite.Group()
        
    def load_sprite_sheets(self, dir1, dir2, width, height, direction = False):
        """
        Carga hojas de sprites desde un directorio, las divide en sprites individuales 
        y las almacena en un diccionario.

        Args:
            dir1 (str): El primer subdirectorio de la ruta de los sprites.
            dir2 (str): El segundo subdirectorio de la ruta de los sprites.
            width (int): El ancho de cada sprite.
            height (int): La altura de cada sprite.
            direction (bool): Indica si se deben cargar sprites para ambas direcciones (izquierda y derecha).

        Returns:
            dict: Un diccionario con los sprites cargados.
        """
        
        path = join("src", "assets", dir1, dir2)
        images = [f for f in listdir(path) if isfile(join(path, f))]
        
        all_sprites = {}
        
        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))
                
            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = self.flip(sprites)
            else:
                all_sprites[image.replace(".png", "")] = sprites

        return all_sprites    
    
    def flip(self, sprites):
        """
        Da vuelta la imagen del sprite.

        Args:
            sprites (list): Una lista de superficies que representan los sprites.

        Returns:
            list: Una lista de superficies de sprites volteadas horizontalmente.
        """
        
         
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    def shoot(self):
        """
        Dispara un láser desde la posición actual del jugador.
        """
        laser = Laser(self.rect.centerx, self.rect.centery - 40, 10, 5, self.direction)
        self.lasers.add(laser)

    def update_lasers(self, enemies, coins):
        """
        Actualiza la lógica de disparo del jugador y maneja las colisiones con enemigos.

        Args:
            enemies (pygame.sprite.Group): El grupo de enemigos.
            coins (pygame.sprite.Group): El grupo de monedas.
        """
        self.lasers.update()
        hits = pygame.sprite.groupcollide(self.lasers, enemies, True, False)
        
        for laser, hit_enemies in hits.items():
            for enemy in hit_enemies:
                if isinstance(enemy, Boss):  
                    enemy.lives -= 1  
                    if enemy.lives <= 0 and enemy.dead:  
                        enemies.remove(enemy)  
                        coin = Coin(enemy.rect.centerx, enemy.rect.centery)  
                        coins.add(coin) 
                else:  
                    enemies.remove(enemy) 
                    coin = Coin(enemy.rect.centerx, enemy.rect.centery)  
                    coins.add(coin) 

    def draw_lasers(self, win):
        #dibujamos el laser
        self.lasers.draw(win)
        
    def jump(self):
        """
        Realiza un salto, ajustando la velocidad vertical y reiniciando el contador de saltos.
        """
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def move(self, dx, dy):
        """
        Mueve al jugador en la dirección especificada.

        Args:
            dx (int): La cantidad de movimiento horizontal.
            dy (int): La cantidad de movimiento vertical.
        """
        
        if 0 <= self.rect.x + dx <= WIDTH - self.rect.width:
            self.rect.x += dx
        if 0 <= self.rect.y + dy <= HEIGHT - self.rect.height:
            self.rect.y += dy
        
    def make_hit(self):
        """
        Maneja el estado del jugador al ser golpeado.
        """
    
        self.hit = True
        self.hit_count = 0
        
    def move_left(self, vel):
        """
        Mueve al jugador hacia la izquierda.

        Args:
            vel (int): La velocidad de movimiento.
        """
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
        
    def move_right(self, vel):
        """
        Mueve al jugador hacia la derecha.

        Args:
            vel (int): La velocidad de movimiento.
        """     
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
            
    def loop(self, fps):
        """
        Actualiza la lógica del jugador, incluyendo la física de caída, 
        el estado de invulnerabilidad y la animación del sprite.

        Args:
            fps (int): La cantidad de cuadros por segundo.
        """
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
            
        if self.hit and pygame.time.get_ticks() - self.invulnerable_time > 1000:  # 1 segundos de invulnerabilidad
            self.hit = False
            self.invulnerable = False
            
        self.fall_count += 1
        self.update_sprite()
        
    def landed(self):
        """
        Reinicia los movimientos y contadores cuando el jugador aterriza.
        """
    
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
        
    def hit_head(self):
        """
        Maneja el estado del jugador al chocar contra un obstáculo, invirtiendo la velocidad vertical.
        """
        self.count = 0
        self.y_vel *= -1
        
    def update_sprite(self):
        """
        Actualiza el sprite del jugador según su estado actual y la dirección.
        """
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        if self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.x_vel != 0:
            sprite_sheet = "run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()
        
    def update(self):
        """
        Actualiza el rectángulo y la máscara del sprite del jugador para colisiones.
        """
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
    def draw(self, win,):
        """
        Dibuja el sprite del jugador en la ventana del juego.
        """
        win.blit(self.sprite, (self.rect.x, self.rect.y))
        