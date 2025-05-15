# 1: Create the board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# 2: Display the board
def display_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# 3: Get player input
def player_input(player, board):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (0, 1, or 2): "))
            col = int(input(f"Player {player} - Enter column (0, 1, or 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Choose numbers between 0 and 2.")
            elif board[row][col] != " ":
                print("That cell is already taken.")
            else:
                return row, col
        except ValueError:
            print("Please enter valid numbers.")

# 4:Check for a win
def check_win(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True


    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True


    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# 5: Check for a tie
def check_tie(board):
    return all(cell != " " for row in board for cell in row)

# 6: Game loop
def play():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        row, col = player_input(current_player, board)
        board[row][col] = current_player

# Check for win
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

# Check for tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

# Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play()
