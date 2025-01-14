def print_board(board):
    print("-----")
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board):
    # check rows
    for row in board:
        if row.count("X") == 3:
            return "X"
        elif row.count("O") == 3:
            return "O"
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    # check for draw
    for row in board:
        if " " in row:
            return None
    return "Draw"

def make_move(board, player):
    while True:
        row = int(input(f"Player {player}, enter the row of your move (0, 1, 2): "))
        col = int(input(f"Player {player}, enter the column of your move (0, 1, 2): "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Try again.")
        elif board[row][col] != " ":
            print("That space is already taken. Try again.")
        else:
            board[row][col] = player
            break
    return board

def game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("First player to get 3 in a row wins!")
    print("Player 1 is X, Player 2 is O")
    print("Good luck!")

    while True:
        print_board(board)
        make_move(board, player)

        if check_winner(board) == "X":
            print("Player 1 wins!")
            break
        elif check_winner(board) == "O":
            print("Player 2 wins!")
            break
        elif check_winner(board) == "Draw":
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

game()
