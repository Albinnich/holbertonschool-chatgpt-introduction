def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] != " " and all(cell == row[0] for cell in row):
            return True

    for col in range(len(board[0])):
        if board[0][col] != " " and all(board[row][col] == board[0][col] for row in range(1, len(board))):
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(1, len(board))):
        return True
    if board[0][len(board) - 1] != " " and all(board[i][len(board) - i - 1] == board[0][len(board) - 1] for i in range(1, len(board))):
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column numbers.")

    print_board(board)
    winner = "0" if player == "X" else "X"
    print("Player " + winner + " wins!")

tic_tac_toe()
