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
    pass


# Function to generate a move for the computer
def generateComputerMove(board, difficulty):
    pass


# Function to initialize the board
def initializeBoard():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]



def playMove(i=None, j=None):  # assining default values to i and j to avoid error if computer plays
    pass

# ----------------------------------------------------------------------

def startingMove():
    pass


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