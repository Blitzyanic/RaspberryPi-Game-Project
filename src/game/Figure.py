import random


class Figure:
    x = 0
    y = 0

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

    # Verschiedene Formen der Tetris-Steine
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # Form 1 (T)
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # Form 2 (S)
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # Form 3 (Z)
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # Form 4 (L)
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # Form 5 (J)
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # Form 6 (O)
        [[1, 2, 5, 6]],  # Form 7 (I)
    ]

    def __init__(self, x, y):
        self.x = x  # X-Position des Steins
        self.y = y  # Y-Position des Steins
        self.type = random.randint(0, len(self.figures) - 1)  # Zufällige Auswahl der Steinform
        self.color = random.randint(1, len(self.colors) - 1)  # Zufällige Farbe des Steins
        self.rotation = 0  # Anfangsrotation ist 0 (keine Drehung)

    def image(self):
        # Gibt die aktuelle Darstellung des Steins basierend auf der Rotation zurück
        return self.figures[self.type][self.rotation]

    def rotate(self):
        # Dreht den Stein im Uhrzeigersinn
        self.rotation = (self.rotation - 1) % len(self.figures[self.type])