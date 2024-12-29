import time
import pyfiglet

def show_ascii_welcome():
    """Функция отображает приветствие в стиле ASCII."""
    ascii_art = pyfiglet.figlet_format("Krestiki Noliki")
    print(ascii_art)
    print("Добро пожаловать в игру Крестики Нолики!")
    print("-" * 50)

field = [[" - "]*3 for _ in range(3)]  # Игровое поле

def print_field():
    """Функция для печати текущего состояния игрового поля."""
    for row in field:
        print("".join(row))

def move_player(player_symbol):
    """Функция обработки хода игрока."""
    while True:
        move = input(f"Ход игрока '{player_symbol}'. Укажите координаты в формате x,y (x — строка, y — столбец, отсчёт начинается с нуля): ")
        if ',' not in move:
            print("Некорректный ввод! Убедитесь, что координаты в формате x,y.")
            continue

        parts = move.split(',')
        if len(parts) != 2:
            print("Некорректный ввод! Укажите ровно две координаты.")
            continue

        if not (parts[0].isdigit() and parts[1].isdigit()):
            print("Координаты должны быть числами!")
            continue

        row, col = int(parts[0]), int(parts[1])
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Координаты должны быть в пределах игрового поля (0, 1, 2).")
            continue

        if field[row][col] != ' - ':
            print("Эта клетка уже занята! Попробуйте снова.")
            continue

        field[row][col] = f' {player_symbol} '
        break
def check_win(): # функция проверки выигрышных комбинаций
    win_options = (
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 1)),
    ) # кортеж, содержит восемь кортежей, каждый из которых содержит три кортежа с координатами выигрышного варианта
    for win in win_options: # проходимся циклом по выигрышным комбинациям
        win_simbols = [] # объявляем список, в который будем добавлять значения клеток по координатам выигрышной комбинации
        for symbol in win: # проходимся циклом по кортежу конкретной выигрышной комбинации
            win_simbols.append(field[symbol[0]][symbol[1]]) # добавляем в список win_simbols значения клеток по координатам выигрышной комбинации
        if win_simbols == ["X", "X", "X"]: # если список win_simbols содержит все X
            print_field() # отображаем игровое поле
            print("Выиграл крестик! (X)") # выводим сообщение о выигрыше крестика
            return True # возвращаем истину
        if win_simbols == ["0", "0", "0"]: # если список win_simbols содержит все 0
            print_field() # отображаем игровое поле
            print("Выиграл нолик! (0)") # выводим сообщение о выигрыше нолика
            return True # возвращаем истину
    return False # возвращаем ложь


def prepare():
    """Подготовка и запуск игры."""
    show_ascii_welcome()
    ask1 = input('Вы готовы к игре? (y = да, n = нет): ')
    if ask1.lower() == 'y':
        time.sleep(1.2)
        print('Начинаем!')
        time.sleep(0.6)

        while True:
            print_field()
            move_player('X')  # Ход первого игрока
            print_field()
            move_player('O')  # Ход второго игрока

prepare()