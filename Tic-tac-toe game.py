# Игра "крестики-нолики". Tic-tac-toe game

# Создаем игровое поле 3х3 для вывода на экран через f-строку. Create a 3x3 playing zone via f-string
def print_gamezone(gamezone):
    print(f'{gamezone[0]}|{gamezone[1]}|{gamezone[2]}\n'
          f'{gamezone[3]}|{gamezone[4]}|{gamezone[5]}\n'
          f'{gamezone[6]}|{gamezone[7]}|{gamezone[8]}')

# Создаем проверку условия победы. Validate win
def check_winner(gamezone, player):
    return ((gamezone[0] == player and gamezone[1] == player and gamezone[2] == player) or
            (gamezone[3] == player and gamezone[4] == player and gamezone[5] == player) or
            (gamezone[6] == player and gamezone[7] == player and gamezone[8] == player) or
            (gamezone[0] == player and gamezone[3] == player and gamezone[6] == player) or
            (gamezone[1] == player and gamezone[4] == player and gamezone[7] == player) or
            (gamezone[2] == player and gamezone[5] == player and gamezone[8] == player) or
            (gamezone[0] == player and gamezone[4] == player and gamezone[8] == player) or
            (gamezone[2] == player and gamezone[4] == player and gamezone[6] == player))

# Основная функция игры. Main fuction of the game
def play_game():
    gamezone = [' '] * 9         # Создание игрового поля. Create game zone.
    players = ['X', 'O']         # Создание игроков. Create players.
    current_player = players[0]  # Определение текущего игрока. Determining the current player.
    winner = False               # Создание флага для цикла. Creating a Flag for a Loop.

    while not winner:
        # Создание извещения о том - кто делает ход. Creating a notification about who makes a move.
        print(f'{current_player} turn:')
        print('_____')

        # Запуск функции печати игровой зоны. Starting the print function of the play area.
        print_gamezone(gamezone)
        print('_____')

        # Запрос выбора зоны. Zone selection request
        choice = int(input('Enter your choice - number 1-9: '))
        print()

        # Проверка условия занятости зоны. Checking the zone busy condition.
        if gamezone[choice - 1] == ' ':
            gamezone[choice - 1] = current_player
        else:
            print(f'Try again. This place is busy!')
            print()
            continue # В случае занятости - повторение запроса. In case of busy - repeat the request.

        # Запуск функции проверки победителя. Starting the check function of winner
        if check_winner(gamezone, current_player):
            print(f'{current_player} wins! Congratulation!')
            winner = True
        elif ' ' not in gamezone:   # Оповещение о ничье. Tie notice
            print(f'Tie in a game')
            break
        else:
            # Сменить игрока. Change player
            current_player = players[(players.index(current_player) + 1) % 2]


if __name__ == "__main__":
    play_game()

