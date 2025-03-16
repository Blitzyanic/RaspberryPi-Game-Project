import pygame
from src.raspberry.Rpi import Rpi

from src.game.Tetris import Tetris


# Farben für die verschiedenen Tetris-Steine
colors = [
    (0, 0, 0),  # Hintergrundfarbe (schwarz)
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

# Initialisiere das Spiel mit pygame
pygame.init()
rpi = Rpi()
rpi.reset_game()

# Farben für das Spiel
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Fenstergröße
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Hauptspielschleife
done = False
clock = pygame.time.Clock()
fps = 25  # Frames pro Sekunde
game = Tetris(20, 10)  # Erstelle ein Tetris-Spiel mit einem Spielfeld von 20x10
counter = 0

previous_lives = game.lives  # Track lives to detect changes

pressing_down = False  # Wird verwendet, um festzustellen, ob der Spieler die Pfeiltaste nach unten gedrückt hält

while not done:
    if game.figure is None:
        game.new_figure()  # Erzeuge einen neuen Tetris-Stein, wenn keiner vorhanden ist
    counter += 1
    if counter > 100000:
        counter = 0

    # Check if player lost a life
    if previous_lives > game.lives:
        rpi.remove_life(previous_lives)
        previous_lives = game.lives

    # Das Spiel bewegt den Stein nach unten, wenn genügend Zeit vergangen ist oder der Spieler nach unten drückt
    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    rpi.process_joystick(game)

    rpi.process_button(game)

    if game.lives == 0 and rpi.get_button():
        game.__init__(20, 10)  # Das Spiel zurücksetzen
        rpi.reset_game()
        previous_lives = game.lives  # Reset the life counter

    # Verarbeite Tasteneingaben
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
                pressing_down = False
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
                pressing_down = False
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
                pressing_down = False
            if event.key == pygame.K_SPACE:
                game.go_space()
                pressing_down = False
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)  # Das Spiel zurücksetzen
                rpi.reset_game()
                previous_lives = game.lives  # Reset the life counter

    # Wenn die nach unten-Taste losgelassen wird, stoppe das Fallen
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    # Bildschirm zeichnen
    screen.fill(BLACK)

    # Zeichne das Spielfeld
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]], 
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    # Zeichne den aktuellen Stein
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color], 
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    # Anzeige von Punkten und Leben
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, WHITE)
    lives_text = font.render("Lives: " + str(game.lives), True, WHITE)  # Anzeige der Leben
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    # Positionierung der Textanzeigen
    screen.blit(text, [0, 0])
    screen.blit(lives_text, [0, 30])  # Anzeige der verbleibenden Leben
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()  # Bildschirm aktualisieren
    clock.tick(fps)  # Framerate einhalten

pygame.quit()  # Beende pygame
