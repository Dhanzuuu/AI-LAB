import random
import time

def show_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print("\n")
    
def check_win(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == player:
            return True

    return False


def check_draw(board):
    return all(x in ["X", "O"] for x in board)


def empty_spaces(board):
    return [i for i in range(9) if board[i] not in ["X", "O"]]


def game():
    board = [str(i) for i in range(1, 10)]

    print("Welcome to Tic-Tac-Toe!")
    show_board(board)

    player = input("Choose X or O: ").upper()

    while player not in ["X", "O"]:
        player = input("Please choose X or O: ").upper()

    computer = "O" if player == "X" else "X"
    turn = "X"

    while True:

        if turn == player:
            choice = int(input("Choose a position (1-9): ")) - 1

            if choice < 0 or choice > 8:
                print("Wrong position!")
                continue

            if board[choice] in ["X", "O"]:
                print("That place is taken!")
                continue

            board[choice] = player

        else:
            print("Computer's turn...")
            time.sleep(1)

            choice = random.choice(empty_spaces(board))
            board[choice] = computer

        show_board(board)

        if check_win(board, turn):
            if turn == player:
                print("You win!")
            else:
                print("Computer wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        if turn == player:
            turn = computer
        else:
            turn = player


game()
