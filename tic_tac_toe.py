# Tic Tac Toe Game

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()


def check_win(board, player):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


while True:
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Player {current_player}, Enter Row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, Enter Column (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Invalid position! Try again.")
                continue

            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue

            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} Wins!")
                break

            if check_tie(board):
                print_board(board)
                print("🤝 Match Draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter valid numbers.")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
