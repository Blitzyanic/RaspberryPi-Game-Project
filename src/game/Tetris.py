from src.game.Figure import Figure


class Tetris:
    def __init__(self, height, width):
        self.level = 2  # Schwierigkeitsgrad (Level)
        self.score = 0  # Spielergebnis
        self.lives = 3  # Anzahl der Leben des Spielers
        self.state = "start"  # Aktueller Spielzustand
        self.field = []  # Spielfeld
        self.height = height  # Höhe des Spielfelds
        self.width = width  # Breite des Spielfelds
        self.x = 100  # X-Offset für das Zeichnen des Spielfelds
        self.y = 60  # Y-Offset für das Zeichnen des Spielfelds
        self.zoom = 20  # Größe eines Blocks
        self.figure = None  # Der aktuelle Tetris-Stein

        # Initialisiere das Spielfeld mit Nullen (leere Felder)
        self.field = [[0 for _ in range(width)] for _ in range(height)]

    def new_figure(self):
        # Erzeugt einen neuen Tetris-Stein
        self.figure = Figure(3, 0)

    def intersects(self):
        # Prüft, ob der aktuelle Stein mit anderen Blöcken oder den Rändern des Spielfelds kollidiert
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        # Überprüft, ob eine Reihe vollständig ausgefüllt ist und entfernt diese
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:  # Eine komplette Reihe
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2  # Punkte basierend auf der Anzahl der entfernten Reihen

    def go_space(self):
        # Der Stein fällt, bis er auf ein Hindernis trifft
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        # Der Stein bewegt sich um eine Reihe nach unten
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        # "Einfrieren" des Steins (wenn er auf einem anderen Stein oder dem Spielfeldboden landet)
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()  # Überprüfe, ob Reihen entfernt werden können
        self.new_figure()  # Erzeuge einen neuen Stein
        if self.intersects():
            # Wenn nach dem Erzeugen des neuen Steins eine Kollision vorliegt, hat der Spieler verloren
            self.lives -= 1  # Ein Leben abziehen
            if self.lives <= 0:
                self.state = "gameover"  # Das Spiel ist vorbei, keine Leben mehr
            else:
                self.reset_game()  # Zurücksetzen des Spiels, aber mit verbleibenden Leben

    def go_side(self, dx):
        # Der Stein bewegt sich nach links (-1) oder rechts (+1)
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        # Der Stein wird rotiert
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation  # Rückgängig machen, wenn die Rotation nicht möglich ist

    def reset_game(self):
        # Setzt das Spielfeld zurück und beginnt mit einem neuen Spiel
        self.field = [[0 for _ in range(self.width)] for _ in range(self.height)]  # Spielfeld zurücksetzen
        self.score = 0  # Punkte zurücksetzen
        self.new_figure()  # Erzeuge einen neuen Tetris-Stein