import keyboard
import os
import random

# Определение символов для отображения на поле
COLS = 25
ROWS = 10
EMPTY = '☐'
PLAYER = 'P'
ANT = 'a'

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

# Класс, представляющий персонажа на поле
class Character:
    def __init__(self, Y=None, X=None, image=None):
        """
        Конструктор класса Character.

        Параметры:
        - Y: Координата Y персонажа.
        - X: Координата X персонажа.
        - image: Символ, представляющий персонажа на поле.
        """
        self.image = image
        self.Y = Y
        self.X = X

    def move(self, direction, field):
        """
        Метод перемещения персонажа в указанном направлении.

        Параметры:
        - direction: Направление движения ('up', 'down', 'left', 'right').
        - field: Объект класса Field, представляющий игровое поле.
        """
        new_Y, new_X = self.Y, self.X

        if direction == 'up' and self.Y > 0:
            new_Y -= 1
        elif direction == 'down' and self.Y < field.rows - 1:
            new_Y += 1
        elif direction == 'left' and self.X > 0:
            new_X -= 1
        elif direction == 'right' and self.X < field.cols - 1:
            new_X += 1

        if field.cells[new_Y][new_X].content is None:
            field.cells[self.Y][self.X].content = None
            self.Y, self.X = new_Y, new_X
            field.cells[self.Y][self.X].content = self

# Класс, представляющий игрока
class Player(Character):
    def __init__(self, Y=None, X=None):
        """
        Конструктор класса Player.

        Параметры:
        - Y: Координата Y игрока.
        - X: Координата X игрока.
        """
        super().__init__(Y, X, image=PLAYER)

# Класс, представляющий муравья
class Ant(Character):
    def __init__(self, Y=None, X=None):
        """
        Конструктор класса Ant.

        Параметры:
        - Y: Координата Y муравья.
        - X: Координата X муравья.
        """
        super().__init__(Y, X, image=ANT)

    def move_away_from_player(self, player, field):
        """
        Метод перемещения муравья в противоположном направлении относительно игрока.

        Параметры:
        - player: Объект класса Player, представляющий игрока.
        - field: Объект класса Field, представляющий игровое поле.
        """
        directions = ['up', 'down', 'left', 'right']
        opposite_directions = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }

        direction = random.choice(directions)
        player_distance = abs(player.Y - self.Y) + abs(player.X - self.X)

        while True:
            self.move(direction, field)

            new_distance = abs(player.Y - self.Y) + abs(player.X - self.X)
            if new_distance >= player_distance:
                break

            direction = opposite_directions[direction]

# Класс, представляющий игровое поле
class Field:
    def __init__(self, cell=Cell, player=Player, ant=Ant):
        """
        Конструктор класса Field.

        Параметры:
        - cell: Класс, представляющий ячейку на поле.
        - player: Класс, представляющий игрока.
        - ant: Класс, представляющий муравья.
        """
        self.rows = ROWS
        self.cols = COLS
        self.cells = [[cell(Y=y, X=x) for x in range(COLS)] for y in range(ROWS)]
        self.player = player(Y=random.randint(0, ROWS - 1), X=random.randint(0, COLS - 1))
        self.ant = ant(Y=random.randint(0, ROWS - 1), X=random.randint(0, COLS - 1))
        self.cells[self.player.Y][self.player.X].content = self.player
        self.cells[self.ant.Y][self.ant.X].content = self.ant

    def drawrows(self):
        """
        Метод отрисовки всех строк игрового поля.
        """
        for row in self.cells:
            for cell in row:
                cell.draw()
            print()

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

    # Обработка событий клавиатуры
    def handle_keyboard_event(self, event):
        """
        Метод обработки событий клавиатуры.

        Параметры:
        - event: Объект события клавиатуры.
        """
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'up':
                self.field.player.move('up', self.field)
                self.field.ant.move_away_from_player(self.field.player, self.field)
            elif event.name == 'down':
                self.field.player.move('down', self.field)
                self.field.ant.move_away_from_player(self.field.player, self.field)
            elif event.name == 'left':
                self.field.player.move('left', self.field)
                self.field.ant.move_away_from_player(self.field.player, self.field)
            elif event.name == 'right':
                self.field.player.move('right', self.field)
                self.field.ant.move_away_from_player(self.field.player, self.field)
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
