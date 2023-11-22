import keyboard
import os
import random

# Определение символов для отображения на поле
COLS = 25
ROWS = 10
EMPTY = '☐'
PLAYER = 'P'
ANT = 'a'
ANTHILL = 'A'
ANTHILL_MAX = 4
ANTHILL_MINI = 1
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

class GameObject:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.image = None

# Класс, представляющий ячейку на поле
class Cell:
    def __init__(self, Y=None, X=None):
        """
        Конструктор класса Cell.

        Параметры:
        - Y: Координата Y ячейки.
        - X: Координата X ячейки.
        """
        self.image = EMPTY
        self.Y = Y
        self.X = X
        self.content = None

    def draw(self):
        """
        Метод отрисовки содержимого ячейки.
        """
        if self.content:
            print(self.content.image, end=' ')
        else:
            print(self.image, end=' ')

# Класс, представляющий игрока
class Player(GameObject):
def __init__(self, y=None, x=None):
        super().__init__(y, x)
        self.image = PLAYER

    def move(self, direction, field):
        new_y, new_x = self.y, self.x

        if direction == UP and self.y > 0 and not isinstance(field.cells[self.y - 1][self.x].content, Anthill):
            new_y -= 1
        elif direction == DOWN and self.y < field.rows - 1 and not isinstance(field.cells[self.y + 1][self.x].content, Anthill):
            new_y += 1
        elif direction == LEFT and self.x > 0 and not isinstance(field.cells[self.y][self.x - 1].content, Anthill):
            new_x -= 1
        elif direction == RIGHT and self.x < field.cols - 1 and not isinstance(field.cells[self.y][self.x + 1].content, Anthill):
            new_x += 1

        # Update the player's position
        field.cells[self.y][self.x].content = None
        self.y, self.x = new_y, new_x
        field.cells[self.y][self.x].content = self

class Anthill(GameObject):
    def __init__(self, x, y, quantity):
        super().__init__(y, x)
        self.image = 'A'
        self.quantity = quantity

    def place_anthill(self, field):
        field.cells[self.y][self.x].content = self

# Класс, представляющий игровое поле
class Field:
    def __init__(self, cell=Cell, player=Player, anthill=Anthill, anthill_max=ANTHILL_MAX, anthill_mini=ANTHILL_MINI):
        # ... (ваш существующий код)
        self.anthills = []
        """
        Конструктор класса Field.

        Параметры:
        - cell: Класс, представляющий ячейку на поле.
        - player: Класс, представляющий игрока.
        - ant: Класс, представляющий муравья.
        """
        self.rows = ROWS
        self.cols = COLS
        self.anthills = []
        self.cells = [[cell(Y=y, X=x) for x in range(COLS)] for y in range(ROWS)]
        self.player = player(y=random.randint(0, ROWS - 1), x=random.randint(0, COLS - 1))
        self.cells[self.player.y][self.player.x].content = self.player

    def drawrows(self):
        """
        Метод отрисовки всех строк игрового поля.
        """
        for row in self.cells:
            for cell in row:
                cell.draw()
            print()

    def add_anthill(self, anthill):
        self.anthills.append(anthill)
        anthill.place_anthill(self)

    def add_anthills_randomly(self):
        for _ in range(random.randint(ANTHILL_MINI, ANTHILL_MAX)):
            anthill = Anthill(x=random.randint(0, COLS - 1), y=random.randint(0, ROWS - 1), quantity=random.randint(ANTHILL_MINI, ANTHILL_MAX))
            self.add_anthill(anthill)

# Функция для очистки экрана консоли
def clear_screen():
    """
    Функция для очистки экрана консоли.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Класс, представляющий игру
class Game:
    def __init__(self):
        """
        Конструктор класса Game.
        """
        self.field = Field()
        self.field.add_anthills_randomly()
    # Обработка событий клавиатуры
    def handle_keyboard_event(self, event):
        """
        Метод обработки событий клавиатуры.

        Параметры:
        - event: Объект события клавиатуры.
        """
    def handle_keyboard_event(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == UP:
                self.field.player.move(UP, self.field)
            elif event.name == DOWN:
                self.field.player.move(DOWN, self.field)
            elif event.name == LEFT:
                self.field.player.move(LEFT, self.field)
            elif event.name == RIGHT:
                self.field.player.move(RIGHT, self.field)
            elif event.name == 'esc':
                print("Выход из игры.")
                return True
        return False

    # Обновление состояния игры
    def update_game_state(self):
        """
        Метод обновления состояния игры.
        """
        clear_screen()
        self.field.drawrows()

    # Запуск игры
    def run(self):
        """
        Метод запуска игры.
        """
        self.field.drawrows()

        while True:
            event = keyboard.read_event(suppress=True)
            if self.handle_keyboard_event(event):
                break

            self.update_game_state()

# Создание экземпляра игры и запуск
game_instance = Game()
game_instance.run()
