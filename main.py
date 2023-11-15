import random


class Cell:
    """
    Класс, представляющий ячейку в игровом поле.

    Attributes:
    image (str): Символ, представляющий изображение ячейки (Default '☐').
    Y (int): Координата по вертикали.
    X (int): Координата по горизонтали.
    content: Содержимое ячейки, например, объект игрока.
    """

    def __init__(self, image='☐', Y=None, X=None):
        """
        Инициализация ячейки.

        Parameters:
        image (str): Символ, представляющий изображение ячейки (Default '☐').
        Y (int): Координата по вертикали.
        X (int): Координата по горизонтали.
        """
        self.image = image
        self.Y = Y
        self.X = X
        self.content = None  # Initialize content to None

class Player:
    """
    Класс, представляющий игрока.

    Attributes:
    image (str): Символ, представляющий изображение игрока (Default 'P').
    Y (int): Координата игрока по вертикали.
    X (int): Координата игрока по горизонтали.
    """

    def __init__(self, image='P', Y=None, X=None):
        """
        Инициализация игрока.

        Parameters:
        image (str): Символ, представляющий изображение игрока (Default 'P').
        Y (int): Координата игрока по вертикали.
        X (int): Координата игрока по горизонтали.
        """
        self.image = image
        self.Y = Y
        self.X = X

class Field:
    # ... (previous code remains unchanged)

    def __init__(self, rows=10, cols=25, cell=Cell, player=Player):
        """
        Инициализация игрового поля.

        Parameters:
        rows (int): Количество строк в поле (Default 10).
        cols (int): Количество столбцов в поле (Default 25).
        cell (Cell): Класс ячейки, используемый для создания полей.
        player (Player): Класс игрока.
        """
        self.rows = rows
        self.cols = cols
        self.cells = [[cell(Y=y, X=x) for x in range(cols)] for y in range(rows)]
        self.player = player(Y=random.randint(0, rows-1), X=random.randint(0, cols-1))
        self.cells[self.player.Y][self.player.X].content = self.player

    def drawrows(self):
        """
        Отображение содержимого полей в виде строк.
        """
        for row in self.cells:
            for cell in row:
                if (cell.Y, cell.X) != (self.player.Y, self.player.X):
                    print(cell.image, end=' ')
                else:
                    print(self.player.image, end=' ')
            print()


MyClass = Field()
MyClass.drawrows()