import pygame
from enemies import Enemy
from constants import HEIGHT
from os import listdir
from os.path import isfile, join
from sounds import *

class Boss(Enemy):
    """Controla el comportamiento del jefe enemigo en el juego."""
    def __init__(self, x, y, width, height, sprites):
        """
        Inicializa una nueva instancia del jefe enemigo.

        Args:
            x (int): La posición horizontal inicial del jefe.
            y (int): La posición vertical inicial del jefe.
            width (int): El ancho del sprite del jefe.
            height (int): La altura del sprite del jefe.
            sprites (dict): Un diccionario de sprites del jefe.
        """
        super().__init__(x, y, width, height, sprites)
        self.lives = 3  # El jefe muere después de 3 golpes
        self.bullets = pygame.sprite.Group()  # Los disparos del jefe
        self.y_vel = 1  # La velocidad vertical del jefe
        self.direction = "left"  # Dirección inicial del jefe
        self.last_shot = pygame.time.get_ticks()  # La última vez que el jefe disparó
        self.bullet_speed = 5 # La velocidad inicial de las balas del jefe
        self.bullet_speed_increased = False
        self.dead = False
        bullet_image = pygame.image.load('./src/assets/Laser/laser_devil.png')  # Carga la imagen del disparo
        self.bullet_image = pygame.transform.scale(bullet_image, (40, 40))  

    def load_enemy_sprites(self, dir1, dir2, width, height, direction=False):
        """
        Carga hojas de sprites del jefe desde un directorio y las divide en sprites individuales.

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
                # Escala cada sprite
                scaled_surface = pygame.transform.scale(surface, (400,600))
                sprites.append(scaled_surface)

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = self.flip(sprites)
            else:
                all_sprites[image.replace(".png", "")] = sprites

        return all_sprites

    def death_animation(self):
        """
        Reproduce la animación de muerte del jefe y marca al jefe como muerto si la animación ha terminado.
        """
        # Cambia los sprites a los sprites de muerte
        sprite_sheet_name = "death_" + self.direction
        sprites = self.sprites[sprite_sheet_name]

        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.animation_count += 1
        sprite = sprites[sprite_index]
        self.image = sprite

        # Si hemos llegado al final de la animación de muerte, marca al jefe como muerto
        if sprite_index == len(sprites) - 1:
            self.dead = True

    def loop(self, objects):
        """
        Actualiza el comportamiento del jefe, incluyendo el movimiento vertical y el disparo.

        Args:
            objects (list): Lista de objetos del juego, como el jugador y otros enemigos.
        """

        # Cambia la dirección si llega a los bordes
        if self.rect.y <= 0 or self.rect.y >= 25:
            self.y_vel = -self.y_vel

        self.move(0, self.y_vel)  # Mueve al jefe verticalmente

        # Siempre usa las animaciones "idle"
        sprite_sheet_name = "idle_" + self.direction
        sprites = self.sprites[sprite_sheet_name]

        # Hace que el jefe dispare
        if self.lives <= 0:
            self.death_animation()
        else:
            self.shoot()

        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.animation_count += 1
        sprite = sprites[sprite_index]
        self.image = sprite
        
    def shoot(self):
        """
        Dispara una bala desde la posición actual del jefe si han pasado más de 2 segundos desde el último disparo.
        """
        now = pygame.time.get_ticks()  # La hora actual
        if now - self.last_shot > 2000:  # Si han pasado más de 2 segundos desde el último disparo
            bullet = BulletBoss(self.rect.centerx, self.rect.centery, -self.bullet_speed, 0, self.bullet_image)  # Crea un nuevo disparo
            self.bullets.add(bullet)  # Añade el disparo al grupo de disparos
            self.last_shot = now  # Actualiza la última vez que el jefe disparó

    def update_bullets(self, player):
        """
        Actualiza los disparos del jefe y maneja las colisiones con el jugador.

        Args:
            player (Player): La instancia del jugador en el juego.
        """
        
        from levels import window, game_over_menu
        self.bullets.update()  # Actualiza los disparos
        for bullet in self.bullets:  # Comprueba si algún disparo ha golpeado al jugador
            if pygame.sprite.collide_rect(player, bullet):
                player.lives -= 1  # Reduce las vidas del jugador
                self.bullets.remove(bullet)  # Elimina el disparo
                if player.lives <= 0:  # Si el jugador no tiene vidas
                    pygame.mixer.music.stop()  # Detén la música de fondo
                    game_over_sound.play()  # Reproduce el sonido de "game over"
                    game_over_menu(window)  # Muestra el menú de game over
                    
                        

    def draw(self, win):
        """
        Dibuja al jefe y sus disparos en la ventana del juego.

        Args:
            win (pygame.Surface): La superficie de la ventana del juego.
        """
        
        super().draw(win)  # Dibuja al jefe
        for bullet in self.bullets:  # Dibuja los disparos
            bullet.draw(win)

class BulletBoss(pygame.sprite.Sprite):
    """Representa las balas disparadas por el jefe enemigo."""
    def __init__(self, x, y, dx, dy, image):
        """
        Inicializa una nueva instancia de una bala disparada por el jefe.

        Args:
            x (int): La posición horizontal inicial de la bala.
            y (int): La posición vertical inicial de la bala.
            dx (int): La velocidad horizontal de la bala.
            dy (int): La velocidad vertical de la bala.
            image (pygame.Surface): La imagen que representa la bala.
        """    
        super().__init__()
        self.image = image  # Usa la imagen pasada como argumento
        self.rect = self.image.get_rect()  # Obtiene el rectángulo del disparo a partir de la imagen
        self.rect.topleft = (x, y)  # Posiciona el disparo
        self.dx = dx  # La velocidad horizontal del disparo
        self.dy = dy  # La velocidad vertical del disparo

    def update(self):
        self.rect.x += self.dx  # Mueve el disparo horizontalmente
        self.rect.y += self.dy  # Mueve el disparo verticalmente

    def draw(self, win):
        win.blit(self.image, self.rect)  # Dibuja el disparo usando la imagen