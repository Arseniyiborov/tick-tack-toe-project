import time

# ASCII-арт приветствия
print(r"""
  _______ _   ___      _______     __      _  __  __ _ 
 |__   __(_) | \ \    / / ____|   / /     | |/ / | | |
    | |   _  | |\ \  / / (___    / /  __ _| ' /  | | |
    | |  | | | | \ \/ / \___ \  / /  / _` |  <   | | |
    | |  | | | |  \  /  ____) |/ /__| (_| | . \  |_|_|
    |_|  |_| |_|   \/  |_____/ \____/\__,_|_|\_\ (_|_)
""")

# Создаем игровое поле
field = [[" - "]*3 for _ in range(3)]

# Функция для отображения игрового поля
def print_field():
    for row in field:
        print("".join(row))

# Функция для проверки выигрышных комбинаций
def check_win():
    win_options = (
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),  # горизонтали
        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),  # вертикали
        ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),  # диагонали
    )
    for win in win_options:
        win_symbols = [field[x][y] for x, y in win]
        if win_symbols == [" X ", " X ", " X "]:
            print_field()
            print("🎉 Победа! Выиграл крестик! (X)")
            return True
        if win_symbols == [" 0 ", " 0 ", " 0 "]:
            print_field()
            print("🎉 Победа! Выиграл нолик! (0)")
            return True
    return False

# Функция для обработки хода игрока
def move_player(player_symbol):
    while True:
        move = input(f"Укажите координаты в формате x,y ({player_symbol}): ").strip()
        if ',' not in move or len(move.split(',')) != 2:
            print("❌ Неверный ввод! Укажите координаты в формате x,y, где x и y — числа от 0 до 2.")
            continue

        row, col = move.split(',')
        if not (row.isdigit() and col.isdigit()):
            print("❌ Неверный ввод! Координаты должны быть числами.")
            continue

        row, col = int(row), int(col)
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("❌ Неверный ввод! Координаты должны быть в диапазоне от 0 до 2.")
            continue

        if field[row][col] == ' - ':
            field[row][col] = f" {player_symbol} "
            print_field()
            break
        else:
            print("❌ Эта клетка уже занята! Попробуйте снова.")

# Основная игровая функция
def game():
    print("🎮 Начинаем игру!")
    print_field()
    for turn in range(9):
        if turn % 2 == 0:
            print("🔵 Ход первого игрока (X):")
            move_player("X")
        else:
            print("🟠 Ход второго игрока (0):")
            move_player("0")

        if check_win():
            print("🏆 Игра завершена!")
            return

    print("🤝 Ничья! Поле заполнено.")

# Функция для подготовки к игре
def prepare():
    ask1 = input("Вы готовы к игре? (y = да, n = нет): ").strip().lower()
    if ask1 == 'y':
        time.sleep(1)
        game()
    else:
        print("👋 До встречи!")

prepare()

