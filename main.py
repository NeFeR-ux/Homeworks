def print_board(board):
    """
    Функция для печати игрового поля в консоль.
    Принимает двумерный список 3x3 и выводит его в красивом формате.
    """
    print("\n  0   1   2")
    for i in range(3):
        print(i, end="  ")
        for j in range(3):
            print(board[i][j], end="  ")
        print()
    print()


def check_game_over(board):
    """
    Функция проверки завершенности игры.
    Возвращает:
    - 'X' если выиграли крестики
    - 'O' если выиграли нолики
    - 'Ничья' если ничья
    - None если игра не завершена
    """
    # Проверка строк
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

    # Проверка столбцов
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            return board[0][j]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Проверка на ничью (нет свободных клеток)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return None  # Игра не завершена

    return 'Ничья'  # Все клетки заполнены, победителя нет


def is_valid_move(board, row, col):
    """
    Функция проверки корректности ввода координат.
    Проверяет, что координаты в пределах поля и клетка свободна.
    """
    # Проверка, что координаты - числа (обработка возможных ошибок)
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        return False

    # Проверка границ поля
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False

    # Проверка, свободна ли клетка
    return board[row][col] == ' '


def play_game():
    """
    Основная функция игры с пользовательским интерфейсом.
    """
    # Создание пустого игрового поля
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Первыми ходят крестики

    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Для хода введите номер строки и столбца (от 0 до 2)")
    print_board(board)

    while True:
        # Запрос хода у текущего игрока
        print(f"Ход игрока {current_player}")

        # Ввод координат с проверкой корректности
        while True:
            try:
                row = input("Введите номер строки (0-2): ")
                col = input("Введите номер столбца (0-2): ")

                if is_valid_move(board, row, col):
                    row = int(row)
                    col = int(col)
                    break
                else:
                    print("Некорректный ход! Клетка должна быть свободна, координаты от 0 до 2.")
            except KeyboardInterrupt:
                print("\nИгра прервана. До свидания!")
                return

        # Выполнение хода
        board[row][col] = current_player
        print_board(board)

        result = check_game_over(board)
        if result:
            if result == 'Ничья':
                print("Ничья! Победила дружба!")
            else:
                print(f"Игрок {result} победил! Поздравляем!")
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

    play_again = input("Хотите сыграть еще? (да/нет): ").lower()
    if play_again == 'да' or play_again == 'yes' or play_again == 'y':
        play_game()


# Запуск игры
if __name__ == "__main__":
    play_game()





