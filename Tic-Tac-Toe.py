import random
#Constant represent an empty cell on board
EMPTY = 0


#Initialize the Tic-Tac-Toe board with all cells empty
Board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]
#Function to check if there's a winner on the board returns the winning letter
def checkWin(Board):
    for i in range(3):
        #Check rows for a win
        if Board[i][0] == Board[i][1] == Board[i][2] != EMPTY:
            return Board[i][0]
        #Check columns for a win
        if Board[0][i] == Board[1][i] == Board[2][i] != EMPTY:
            return Board[0][i]
        #Check diagonals for a win
    if Board[0][0] == Board[1][1] == Board[2][2] != EMPTY:
        return Board[0][0]
    if Board[0][2] == Board[1][1] == Board[2][0] != EMPTY:
        return Board[0][2]
    return None #no winner yet

#Function to generate a move for the computer
def generateComputerMove(board, turn, difficulty):
    """
    https://dev.to/lukap/building-an-unbeatable-tic-tac-toe-ai-player-p0f?utm_source
    Generates a move for the computer using a simple strategy.
    - if there is a winning move, play it
    - if there is a move that blocks the opponent's potential win, play it
    - take center if available
    - take a corner if available
    - take a side if available
    """

    if difficulty == 'easy':
        return random.randint(1, 9) #Generate a random move
    #Determine computer and player symbols based on turn True means player is O
    else:
        if turn:
            computer_symbol = 'X'
            player_symbol = 'O'
        else:
            computer_symbol = 'O'
            player_symbol = 'X'

        #1. Check if the computer can win in the next move
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = computer_symbol
                    if checkWin(board) == computer_symbol:
                        board[i][j] = EMPTY  # Undo the move
                        return (i * 3 + j + 1)
                    board[i][j] = EMPTY  # Undo the move

        #2. Check if the player is about to win and block them
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = player_symbol
                    if checkWin(board) == player_symbol:
                        board[i][j] = EMPTY  # Undo the move
                        return (i * 3 + j + 1)
                    board[i][j] = EMPTY  # Undo the move

        #3. Take the center if it's available
        if board[1][1] == EMPTY:
            return 5

        #4. Take a corner if available
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for (i, j) in corners:
            if board[i][j] == EMPTY:
                return (i * 3 + j + 1)

        #5. Take a side if nothing else is available
        sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
        for (i, j) in sides:
            if board[i][j] == EMPTY:
                return (i * 3 + j + 1)

        return None  #No valid moves left (board is full)




#Function to initialize the board
def initializeBoard():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

#Function to ask the player if they want to make the first move
def firstMove():
    while True:
        x = input("do you want to play the first move(y/n): ")
        x = x.lower()
        if x == 'y':
            return True #Player makes the first move
        elif x == 'n':
            return False #Computer makes the first move
        else:
            print("Invalid Input")

#Function to ask the player which symbol they want to use (X or O)
def startingMove():
    while True:
        x = input("enter the starting move(X, O): ")
        x = x.upper()
        if x == 'X':
            return True  #Player chooses X
        elif x == 'O':
            return False  #Player chooses O
        else:
            print("Invalid Input")

#Function to display the move positions on the board
def moves():
    print("""
          1 | 2 | 3
          ----------
          4 | 5 | 6
          ----------
          7 | 8 | 9
          """)

#Function to print the current state of the board
def printBoard(Board):
    print("\n\n-----------------------\n\n")
    for i in range(3):
        for j in range(3):
            if Board[i][j] != EMPTY:
                play = Board[i][j]  #Display X or O
            else:
                play = " "  #Display empty space

            if j == 2:
                print(" ", play)
            else:
                print(" ", play, " |", end="")

        if i != 2:
            print("-" * 20)




#Function to check if a move is invalid
def isInvalidMove(x):
    x = str(x)
    if not x.isdigit() :    #Check if input is a number
        return True

    x = int(x)
    if x < 1 or x > 9:   #Check if input is within the valid range (1-9)
        return True
    else:
        return False

#Function to play a move on the board
def playMove(turn, opponent, difficulty = '', computerTurn = False):
    while True:
        if not opponent and computerTurn:
            x = generateComputerMove(Board, turn, difficulty)   #Generate computer move
        else:
            x = input('Enter the number where you want to place your move (1-9): ')

        if isInvalidMove(x):    #Check if the move is invalid
            print("Invalid Move")
            continue

        x = int(x)
        row = (x - 1) // 3
        col = (x - 1) % 3

        if Board[row][col] != EMPTY:    #Check if the cell is already occupied
            if not computerTurn:
                print("Invalid Move")
            continue
        else:
            if turn:
                Board[row][col] = 'X'   #Place X on the board
                return False
            else:
                Board[row][col] = 'O'   #Place O on the board
                return True

#Function to manage the game
def game(turn, multiPlayer = True, difficulty = '', computerTurn = False):
    moves()     #Display move positions
    for i in range(9):  #Maximum of 9 moves in Tic-Tac-Toe
        printBoard(Board)   #Print the current board state
        turn = playMove(turn, opponent, difficulty, computerTurn)   #Play a move
        if not multiPlayer:
            computerTurn = not computerTurn #Alternate turns in singleplayer mode

        #Check if there's a winner
        if checkWin(Board) == 'X':
            printBoard(Board)   #Print the final board state
            print('\U0001F44F'*25)
            print("Player X Wins")
            print('\U0001F44F' * 25)
            return
        elif checkWin(Board) == 'O':
            printBoard(Board) #Print the final board state
            print('\U0001F44F'*25)
            print("Player O Wins")
            print('\U0001F44F' * 25)
            return

    printBoard(Board) #Print the final board state
    print('\U0001F613' * 25)
    print("It's a tie") #If no winner after 9 moves, it's a tie
    print('\U0001F613' * 25)

#Main game loop
while True:
    play = input("Do you want to play a game with a friend(1) or a computer(2) enter 0 to exit? ")
    if play == '1':
        opponent = True #Play against a friend
        Board = initializeBoard() #Initialize the board
        game(startingMove()) #Start the game and determine starting symbol
    elif play == '2':
        opponent = False  #Play against the computer
        Board = initializeBoard() #Initialize the board
        computerTurn = not firstMove() #Determine if the computer goes first
        startingPlayer = startingMove() #Determine starting player symbol
        while True:
            difficulty = input("Enter the difficulty(easy, hard): ")
            if difficulty.lower() == 'easy' or difficulty.lower() == 'hard':
                game(startingPlayer, False, difficulty , computerTurn) #Start the game with chosen difficulty
                break
            else:
                print("Invalid Input")
                continue
    elif play == '0':
        break #Exit the game
    else:
        print("Invalid Input")
        continue
