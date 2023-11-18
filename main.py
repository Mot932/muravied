COLS = 25
ROWS = 10
EMPTY = '☐'
PLAYER = 'P'
ANTHILL = 'A'
ANT = 'a'

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

    def __init__(self, Y=None, X=None):
        """
        Инициализация ячейки.

        Parameters:
        image (str): Символ, представляющий изображение ячейки (Default '☐').
        Y (int): Координата по вертикали.
        X (int): Координата по горизонтали.
        """
        self.image = EMPTY
        self.Y = Y
        self.X = X
        self.content = None  

    def draw(self):
        if self.content:
            print(self.content.image, end=' ')
        else:
            print(self.image, end=' ')

class Player:
    """
    Класс, представляющий игрока.

    Attributes:
    image (str): Символ, представляющий изображение игрока (Default 'P').
    Y (int): Координата игрока по вертикали.
    X (int): Координата игрока по горизонтали.
    """

    def __init__(self, Y=None, X=None):
        """
        Инициализация игрока.

        Parameters:
        image (str): Символ, представляющий изображение игрока (Default 'P').
        Y (int): Координата игрока по вертикали.
        X (int): Координата игрока по горизонтали.
        """
        self.image = PLAYER
        self.Y = Y
        self.X = X

class Field:

    def __init__(self, cell=Cell, player=Player):
        """
        Инициализация игрового поля.

        Parameters:
        rows (int): Количество строк в поле (Default 10).
        cols (int): Количество столбцов в поле (Default 25).
        cell (Cell): Класс ячейки, используемый для создания полей.
        player (Player): Класс игрока.
        """
        self.rows = ROWS
        self.cols = COLS
        self.cells = [[cell(Y=y, X=x) for x in range(COLS)] for y in range(ROWS)]
        self.player = player(Y=random.randint(0, ROWS-1), X=random.randint(0, COLS-1))
        self.cells[self.player.Y][self.player.X].content = self.player

    def drawrows(self):
        """
        Отображение содержимого полей в виде строк.
        """
        for row in self.cells:
            for cell in row:
                cell.draw()
            print()


MyClass = Field()
MyClass.drawrows()
