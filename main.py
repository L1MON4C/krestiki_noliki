def pole():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def play():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты!")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите цифры!")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты не существуют!")
            continue
        if field[x][y] != " ":
            print(" Клетка занята!")
            continue
        return x, y


def checking_win():
    win_cordinates = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cordinates:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграли Крестики")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли Нолики")
            return True
    return False


field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    pole()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    x, y = play()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if checking_win():
        break
    if count == 9:
        print(" Ничья!")
        break
