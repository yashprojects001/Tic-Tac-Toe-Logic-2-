# STEP 1: Board Representation
# 0 = empty, 1 = Human (X), 2 = AI (O)

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

# STEP 2: Display Board

def print_board(board):
    symbols = [' ', 'X', 'O']
    print()
    for i in range(0, 9, 3):
        print(" ", symbols[board[i]], "|", symbols[board[i+1]], "|", symbols[board[i+2]])
        if i < 6:
            print(" ---+---+---")
    print()

print_board(board)

# STEP 3: Winning Positions

win_positions = [
    (0,1,2), (3,4,5), (6,7,8),   # rows
    (0,3,6), (1,4,7), (2,5,8),   # columns
    (0,4,8), (2,4,6)             # diagonals
]

# STEP 4: POSSWIN Function
# Returns winning position if possible, else -1

def posswin(player):
    for a, b, c in win_positions:
        line = [board[a], board[b], board[c]]
        if line.count(player) == 2 and line.count(0) == 1:
            return [a, b, c][line.index(0)]
    return -1

# STEP 5: AI Move Logic (Logic-2)

def ai_move():
    # Rule 1: Try to win
    move = posswin(2)
    if move != -1:
        return move

    # Rule 2: Block opponent
    move = posswin(1)
    if move != -1:
        return move

    # Rule 3: Take center
    if board[4] == 0:
        return 4

    # Rule 4: Take a corner
    for i in [0, 2, 6, 8]:
        if board[i] == 0:
            return i

    # Rule 5: Take any side
    for i in [1, 3, 5, 7]:
        if board[i] == 0:
            return i

# STEP 6: Human Move

def human_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == 0:
            return move
        print("Invalid move. Try again.")

# STEP 7: Check Winner

def check_winner(player):
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# STEP 8: Main Game Loop

turn = 0

while True:
    print_board(board)

    # Human turn
    board[human_move()] = 1
    turn += 1

    if check_winner(1):
        print_board(board)
        print("🎉 You win!")
        break

    if turn == 9:
        print("It's a draw!")
        break

    # AI turn
    ai = ai_move()
    board[ai] = 2
    turn += 1

    if check_winner(2):
        print_board(board)
        print("🤖 AI wins!")
        break
