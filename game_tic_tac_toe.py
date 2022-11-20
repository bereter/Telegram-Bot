def matrix(con):
    print(f"    1  2  3")
    for lines in range(3):
        print(f" {lines + 1}  {'  '.join(con[lines])}")


def entry():
    while True:
        x = input('Введите номер линии : ')
        y = input('Введите номер колонны : ')
        if len(x) != 1 or len(y) != 1:
            print('Не правильный ввод! Введите одно значение!')
            continue
        if (not x.isdigit()) or (not y.isdigit()):
            print('Не правильный ввод! Введите цифры!')
            continue
        x, y = int(x), int(y)
        x -= 1
        y -= 1
        if 0 > x or x > 3 or 0 > y or y > 3:
            print('Не правильный ввод!')
            continue
        if console[x][y] != '-':
            print('Не правильный ввод! Клетка занята!')
            continue
        return x, y


def win():
    for q in range(3):
        value_win = []
        for w in range(3):
            value_win.append(console[q][w])
        if value_win == ['X', 'X', 'X']:
            print('Выиграл X !!!')
            return True
        elif value_win == ['O', 'O', 'O']:
            print('Выиграл O !!!')
            return True

    for q in range(3):
        value_win = []
        for w in range(3):
            value_win.append(console[w][q])
        if value_win == ['X', 'X', 'X']:
            print('Выиграл X !!!')
            return True
        elif value_win == ['O', 'O', 'O']:
            print('Выиграл O !!!')
            return True

    for q in range(3):
        value_win = []
        for w in range(3):
            value_win.append(console[w][w])
        if value_win == ['X', 'X', 'X']:
            print('Выиграл X !!!')
            return True
        elif value_win == ['O', 'O', 'O']:
            print('Выиграл O !!!')
            return True

    for q in range(3):
        value_win = []
        for w in range(3):
            value_win.append(console[w][2 - w])
        if value_win == ['X', 'X', 'X']:
            print('Выиграл X !!!')
            return True
        elif value_win == ['O', 'O', 'O']:
            print('Выиграл O !!!')
            return True


console = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

motion = 0
print('Добро пожаловать в игру крестики нолики!')

while True:
    matrix(console)
    motion += 1
    if motion % 2 == 1:
        print('Ходит крестик.')
    else:
        print('Ходит нолик.')

    x, y = entry()

    if motion % 2 == 1:
        console[x][y] = 'X'
    else:
        console[x][y] = 'O'

    if win():
        break

    if motion == 9:
        print('Ничья!')
        break
