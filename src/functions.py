import pygame
from os import listdir
from os.path import isfile, join
from constants import *
from sounds import *

def handle_vertical_collision(player, objects, dy):
<<<<<<< HEAD
    """
    Maneja la colisión vertical entre el jugador y los objetos del juego.
    
    Esta función ajusta la posición del jugador según la dirección del movimiento vertical 
    (`dy`) y llama a los métodos adecuados (`landed` o `hit_head`) si se produce una colisión 
    con un objeto.

    Args:
        player (pygame.sprite.Sprite): La instancia del jugador.
        objects (list): Lista de objetos con los que el jugador puede colisionar.
        dy (int): La distancia a mover al jugador en la dirección vertical.

    Returns:
        list: Lista de objetos con los que el jugador ha colisionado.
    """
    
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects

def collide(player, objects, dx):
<<<<<<< HEAD
    """
    Verifica si el jugador colisiona con algún objeto al moverse horizontalmente.

    Esta función mueve temporalmente al jugador en la dirección horizontal especificada
    (`dx`), verifica si colisiona con algún objeto, y luego mueve al jugador de vuelta a 
    su posición original.

    Args:
        player (pygame.sprite.Sprite): La instancia del jugador.
        objects (list): Lista de objetos con los que el jugador puede colisionar.
        dx (int): La distancia a mover al jugador en la dirección horizontal.

    Returns:
        pygame.sprite.Sprite: El primer objeto con el que el jugador colisiona, o None si no hay colisión.
    """
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object

def get_background(name):
<<<<<<< HEAD
    """
    Carga la imagen de fondo y genera una lista de posiciones para los tiles del fondo.

    Esta función carga una imagen de fondo, calcula cuántos tiles de fondo son necesarios
    para cubrir la ventana del juego, y devuelve una lista de posiciones para estos tiles 
    junto con la imagen del fondo.

    Args:
        name (str): El nombre del archivo de la imagen de fondo.

    Returns:
        tuple: Una tupla que contiene:
            - list: Lista de posiciones para los tiles del fondo.
            - pygame.Surface: La imagen del fondo.
    """
    
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
    image = pygame.image.load(join("src", "assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
            
    return tiles, image

def handle_move(player, objects, enemies, coins):
<<<<<<< HEAD
    """
    Maneja el movimiento del jugador y la interacción con objetos, enemigos y disparos.

    Esta función actualiza la velocidad y la dirección del jugador según las teclas presionadas,
    maneja las colisiones horizontales y verticales con objetos y enemigos, y gestiona el disparo 
    del jugador y su interacción con los enemigos y las monedas.

    Args:
        player (pygame.sprite.Sprite): La instancia del jugador.
        objects (list): Lista de objetos con los que el jugador puede colisionar.
        enemies (list): Lista de enemigos en el juego.
        coins (pygame.sprite.Group): Grupo de monedas en el juego.
    """
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
    keys = pygame.key.get_pressed()
    
    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)
    
    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)
    if keys[pygame.K_f] and len(player.lasers) < 1:  # Limite de disparos simultáneos
        player.shoot()
        
    player.update_lasers(enemies, coins)
        
    handle_vertical_collision(player, objects, player.y_vel)

    # Verificar la colisión con los enemigos
    player_rect = player.rect
    
    for enemy in enemies:
        enemy_rect = enemy.rect
        if player_rect.colliderect(enemy_rect):
            player.make_hit()  # Activa el estado de golpe del jugador

def draw(window, background, bg_image, player, objects, enemies, coins, elapsed_time, score):
<<<<<<< HEAD
    """
    Dibuja el fondo, los objetos, el jugador, los enemigos, las monedas y la interfaz en la ventana del juego.

    Esta función se encarga de renderizar todos los elementos del juego en la ventana,
    incluyendo el fondo, los objetos, el jugador, los enemigos, las monedas, el tiempo transcurrido,
    la puntuación y las vidas del jugador.

    Args:
        window (pygame.Surface): La superficie de la ventana del juego.
        background (list): Lista de posiciones para los tiles del fondo.
        bg_image (pygame.Surface): La imagen del fondo.
        player (pygame.sprite.Sprite): La instancia del jugador.
        objects (list): Lista de objetos en el juego.
        enemies (list): Lista de enemigos en el juego.
        coins (pygame.sprite.Group): Grupo de monedas en el juego.
        elapsed_time (float): El tiempo transcurrido desde el inicio del juego.
        score (int): La puntuación actual del jugador.
    """
=======
>>>>>>> 5f6ab14ab925bbc8f971a77440cca031ecb5b247
    for tile in background:
        window.blit(bg_image, tile)
        
    for obj in objects:
        obj.draw(window)
         
    # Dibuja cada enemigo
    for enemy in enemies:
        enemy.draw(window)
        
    for coin in coins:
        window.blit(coin.image, coin.rect) 
    
    player.draw(window)
    player.draw_lasers(window)
    
    # Dibuja el tiempo en la pantalla
    font = pygame.font.SysFont("Minecraft", 25)
    minutes = int(elapsed_time) // 60
    seconds = int(elapsed_time) % 60
    text = font.render("{:02d}:{:02d}".format(minutes, seconds), True, (WHITE))
    text_rect = text.get_rect(center=(WIDTH / 2, 20))  # Obtiene un rectángulo con el centro en (WIDTH / 2, 10)
    window.blit(text, text_rect)

    # Dibuja la puntuación en la pantalla
    score_text = font.render("Puntos: " + str(score), True, (WHITE))
    score_rect = score_text.get_rect(top=10, right=WIDTH - 10)  # Obtiene un rectángulo con el centro en (WIDTH / 2, 50)
    window.blit(score_text, score_rect)
    
    lives_text = font.render("Vidas: " + str(player.lives), True, (WHITE))
    lives_rect = lives_text.get_rect(top=10, left=10)  # Obtiene un rectángulo con la parte superior a 10 y alineado a la izquierda
    window.blit(lives_text, lives_rect) 

    pygame.display.update()