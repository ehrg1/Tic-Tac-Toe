import random

EMPTY = 0



Board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]


def initializeBoard():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

def firstMove():
    while True:
        x = input("do you want to play the first move(y/n): ")
        x = x.lower()
        if x == 'y':
            return True
        elif x == 'n':
            return False
        else:
            print("Invalid Input")


def startingMove():
    while True:
        x = input("enter the starting move(X, O): ")
        x = x.upper()
        if x == 'X':
            return True
        elif x == 'O':
            return False
        else:
            print("Invalid Input")


def moves():
    print("""
          1 | 2 | 3
          ----------
          4 | 5 | 6
          ----------
          7 | 8 | 9
          """)


def printBoard(Board):
    print("\n\n-----------------------\n\n")
    for i in range(3):
        for j in range(3):
            if Board[i][j] != EMPTY:
                play = Board[i][j]
            else:
                play = " "

            if j == 2:
                print(" ", play)
            else:
                print(" ", play, " |", end="")

        if i != 2:
            print("-" * 20)



def checkWin(Board):
    for i in range(3):
        if Board[i][0] == Board[i][1] == Board[i][2] != EMPTY:
            printBoard(Board)
            print('\U0001F44F' * 25)
            print("Player", Board[i][0], "Wins")
            print('\U0001F44F' * 25)
            return True
        if Board[0][i] == Board[1][i] == Board[2][i] != EMPTY:
            printBoard(Board)
            print('\U0001F44F' * 25)
            print("Player", Board[0][i], "Wins")
            print('\U0001F44F' * 25)
            return True
    if Board[0][0] == Board[1][1] == Board[2][2] != EMPTY:
        printBoard(Board)
        print('\U0001F44F'*25)
        print("Player", Board[0][0], "Wins")
        print('\U0001F44F' * 25)
        return True
    if Board[0][2] == Board[1][1] == Board[2][0] != EMPTY:
        printBoard(Board)
        print('\U0001F44F'*25)
        print("Player", Board[0][2], "Wins")
        print('\U0001F44F' * 25)
        return True
    return False


def isInvalidMove(x):
    x = str(x)
    if not x.isdigit() :
        return True

    x = int(x)
    if x < 1 or x > 9:
        return True
    else:
        return False


def playMove(turn, opponent, computerTurn = False):
    while True:
        if not opponent and computerTurn:
            x = random.randint(1, 9) #generate a random move for computer turn
        else:
            x = input('Enter the number where you want to place your move (1-9): ')

        if isInvalidMove(x):
            print("Invalid Move")
            continue

        x = int(x)
        row = (x - 1) // 3
        col = (x - 1) % 3

        if Board[row][col] != EMPTY:
            if not computerTurn:
                print("Invalid Move")
            continue
        else:
            if turn:
                Board[row][col] = 'X'
                return False
            else:
                Board[row][col] = 'O'
                return True


def game(turn, singleGame = True, computerTurn = False):
    moves()
    for i in range(9):
        printBoard(Board)
        turn = playMove(turn, opponent, computerTurn)
        if not singleGame:
            computerTurn = not computerTurn

        if checkWin(Board):
            return

    printBoard(Board)

    print('\U0001F613' * 25)
    print("It's a tie")
    print('\U0001F613' * 25)


while True:
    play = input("Do you want to play a game with a friend(1) or a computer(2) enter 0 to exit? ")
    if play == '1':
        opponent = True
        Board = initializeBoard()
        game(startingMove())
    elif play == '2':
        opponent = False
        Board = initializeBoard()
        computerTurn = not firstMove()
        game(startingMove(),False , computerTurn)
    elif play == '0':
        break
    else:
        print("Invalid Input")
        continue
