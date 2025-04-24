from tkinter import *
from tkinter import messagebox
import random

# Constant represent an empty cell on board
EMPTY = 0
turn = True
opponent = False
difficulty = ''
computerTurn = False
totalMoves = 0

# Initialize the Tic-Tac-Toe board with all cells empty
BoardGUI = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

Board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]


# Function to check if there's a winner on the board returns the winning letter
def checkWin(Board):
    for i in range(3):
        # Check rows for a win
        if Board[i][0] == Board[i][1] == Board[i][2] != EMPTY:
            return Board[i][0]
        # Check columns for a win
        if Board[0][i] == Board[1][i] == Board[2][i] != EMPTY:
            return Board[0][i]
        # Check diagonals for a win
    if Board[0][0] == Board[1][1] == Board[2][2] != EMPTY:
        return Board[0][0]
    if Board[0][2] == Board[1][1] == Board[2][0] != EMPTY:
        return Board[0][2]
    return None  # no winner yet


# Function to generate a move for the computer
def generateComputerMove(board, difficulty):
    """
    https://dev.to/lukap/building-an-unbeatable-tic-tac-toe-ai-player-p0f?utm_source
    Generates a move for the computer using a simple strategy.
    - if there is a winning move, play it
    - if there is a move that blocks the opponent's potential win, play it
    - take center if available
    - take a corner if available
    - take a side if available
    """

    if difficulty == 0:
        return random.randint(1, 9)  # Generate a random move
    # Determine computer and player symbols based on turn True means player is O
    else:
        if turn:
            computer_symbol = 'X'
            player_symbol = 'O'
        else:
            computer_symbol = 'O'
            player_symbol = 'X'

        # 1. Check if the computer can win in the next move
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = computer_symbol
                    if checkWin(board) == computer_symbol:
                        board[i][j] = EMPTY  # Undo the move
                        return (i * 3 + j + 1)
                    board[i][j] = EMPTY  # Undo the move

        # 2. Check if the player is about to win and block them
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = player_symbol
                    if checkWin(board) == player_symbol:
                        board[i][j] = EMPTY  # Undo the move
                        return (i * 3 + j + 1)
                    board[i][j] = EMPTY  # Undo the move

        # 3. Take the center if it's available
        if board[1][1] == EMPTY:
            return 5

        # 4. Take a corner if available
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for (i, j) in corners:
            if board[i][j] == EMPTY:
                return (i * 3 + j + 1)

        # 5. Take a side if nothing else is available
        sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
        for (i, j) in sides:
            if board[i][j] == EMPTY:
                return (i * 3 + j + 1)

        return None  # No valid moves left (board is full)


# Function to initialize the board
def initializeBoard():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]


def winner():
    winnerSympol = checkWin(Board)
    if winnerSympol == None:
      if totalMoves == 9:
          messagebox.showinfo("GameOver", "It's a draw!")
          for i in range(3):
              for j in range(3):
                  BoardGUI[i][j]['state'] = DISABLED
          return True
      else:
          return False
    else:
        if computerTurn:
            messagebox.showinfo("GameOver", "Computer wins!")
            for i in range(3):
                for j in range(3):
                    BoardGUI[i][j]['state'] = DISABLED
            return True

        if winnerSympol == 'X':
            messagebox.showinfo("Winner", "Player X wins!")
            for i in range(3):
                for j in range(3):
                    BoardGUI[i][j]['state'] = DISABLED
            return True
        elif winnerSympol == 'O':
            messagebox.showinfo("Winner", "Player O wins!")
            for i in range(3):
                for j in range(3):
                    BoardGUI[i][j]['state'] = DISABLED
            return True


def playMove(i=None, j=None):  # assining default values to i and j to avoid error if computer plays
    global turn, opponent, difficulty, computerTurn, totalMoves
    while True:
        if opponent == 1 and computerTurn:
            move = generateComputerMove(Board, difficulty)
            if move is not None:
                i = (move - 1) // 3
                j = (move - 1) % 3

        if BoardGUI[i][j]['text'] == "" and BoardGUI[i][j]['state'] == NORMAL:
            if turn:
                BoardGUI[i][j]['text'] = 'X'
                Board[i][j] = 'X'
                turn = not turn
            else:
                BoardGUI[i][j]['text'] = 'O'
                Board[i][j] = 'O'
                turn = not turn
            totalMoves += 1
            BoardGUI[i][j]['state'] = DISABLED
            if winner():
                startButton['state'] = NORMAL
                startButton['bg'] = 'green'
                startButton['text'] = 'Play Again'
                return

            if opponent == 1 and computerTurn:
                computerTurn = False
            elif opponent == 1 and (not computerTurn):
                computerTurn = True
                playMove()

            return


# ----------------------------------------------------------------------

def startingMove():
    global turn, opponent, difficulty, computerTurn, Board, totalMoves
    for i in range(3):
        for j in range(3):
            BoardGUI[i][j]['text'] = ""
            BoardGUI[i][j]['state'] = NORMAL

    startButton['state'] = DISABLED
    startButton['bg'] = 'gray'
    turn = startMoveValue.get()
    opponent = gameTypeValue.get()
    difficulty = gameDifficultyValue.get()
    totalMoves = 0
    Board = initializeBoard()
    if opponent == 1 and startingPlayerValue.get() == 0:
        computerTurn = False
    elif opponent == 1 and startingPlayerValue.get() == 1:
        computerTurn = True
        playMove()



startMove = ['O', 'X']
gameType = ['Player vs Player', 'Player vs Computer']
startingPlayer = ['Player 1', 'computer']
gameDifficulty = ['Easy', 'Hard']

window = Tk()
window.title("Tic Tac Toe")
# window.geometry("400x450")
window.configure(bg="white")
window.resizable(False, False)

# making the options frame
obtionsFrame = Frame(window, height=5, bg='pink')

Label(obtionsFrame,
      text="Starting Move",
      font=("Arial", 13),
      bg="green").grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

startMoveValue = IntVar()
for i in range(len(startMove)):
    startMoveRadio = Radiobutton(obtionsFrame,
                                 text=startMove[i],
                                 variable=startMoveValue,
                                 value=i,
                                 bg="green",
                                 indicatoron=False,
                                 width=15)
    startMoveRadio.grid(row=0, column=i + 1, sticky='nsew')

Label(obtionsFrame,
      text="Game Type",
      font=("Arial", 13),
      bg="green").grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

gameTypeValue = IntVar()
for i in range(len(gameType)):
    gameTypeRadio = Radiobutton(obtionsFrame,
                                text=gameType[i],
                                variable=gameTypeValue,
                                value=i,
                                bg="green",
                                indicatoron=False,
                                width=15, )
    gameTypeRadio.grid(row=1, column=i + 1, sticky='nsew')

Label(obtionsFrame,
      text="Starting Player",
      font=("Arial", 13),
      bg="green").grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

startingPlayerValue = IntVar()
for i in range(len(startingPlayer)):
    startingPlayerRadio = Radiobutton(obtionsFrame,
                                      text=startingPlayer[i],
                                      variable=startingPlayerValue,
                                      value=i,
                                      bg="green",
                                      indicatoron=False,
                                      width=15, )
    startingPlayerRadio.grid(row=2, column=i + 1, sticky='nsew')

Label(obtionsFrame,
      text="Game Difficulty",
      font=("Arial", 13),
      bg="green").grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

gameDifficultyValue = IntVar()
for i in range(len(gameDifficulty)):
    gameDifficultyRadio = Radiobutton(obtionsFrame,
                                      text=gameDifficulty[i],
                                      variable=gameDifficultyValue,
                                      value=i,
                                      bg="green",
                                      indicatoron=False,
                                      width=15, )
    gameDifficultyRadio.grid(row=3, column=i + 1, sticky='nsew')

startButton = Button(obtionsFrame,
                     text="Start Game",
                     bg="green",
                     font=("Arial", 13),
                     state=ACTIVE,
                     command=startingMove)
startButton.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

obtionsFrame.grid(row=0, column=0, columnspan=3)

# making the board frame
boardFrame = Frame(window, bg='gray')

for i in range(3):
    for j in range(3):
        BoardGUI[i][j] = Button(boardFrame,
                                text="",
                                font=("Arial", 13),
                                width=12,
                                height=2,
                                bg="blue",
                                activebackground="red",
                                state=DISABLED,
                                command=lambda row=i, column=j: playMove(row, column))
        BoardGUI[i][j].grid(row=i, column=j, padx=2, pady=2, sticky='nsew')

boardFrame.grid(row=1, column=0, columnspan=3, sticky='nsew')

window.mainloop()