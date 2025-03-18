import random

Board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

turn = True  # Initialize turn variable
opponent = True  # Initialize opponent variable
computerTurn = False  # Initialize computerMove variable

def initializeBoard():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
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
            if Board[i][j] != 0:
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
        if Board[i][0] == Board[i][1] == Board[i][2] != 0:
            printBoard(Board)
            print('\U0001F44F' * 25)
            print("Player", Board[i][0], "Wins")
            print('\U0001F44F' * 25)
            return True
        if Board[0][i] == Board[1][i] == Board[2][i] != 0:
            printBoard(Board)
            print('\U0001F44F' * 25)
            print("Player", Board[0][i], "Wins")
            print('\U0001F44F' * 25)
            return True
    if Board[0][0] == Board[1][1] == Board[2][2] != 0:
        printBoard(Board)
        print('\U0001F44F'*25)
        print("Player", Board[0][0], "Wins")
        print('\U0001F44F' * 25)
        return True
    if Board[0][2] == Board[1][1] == Board[2][0] != 0:
        printBoard(Board)
        print('\U0001F44F'*25)
        print("Player", Board[0][2], "Wins")
        print('\U0001F44F' * 25)
        return True
    return False


def checkMove(x):
    x = str(x)
    if not x.isdigit() :
        return True

    x = int(x)
    if x < 1 or x > 9:
        return True
    else:
        return False


def playMove():
    global turn, opponent, computerTurn
    if not opponent and computerTurn:
        x = random.randint(1, 9) #generate a random move for computer turn
    else:
        x = input('Enter the number where you want to place your move (1-9): ')

    if checkMove(x):
        print("Invalid Move")
        playMove()
        return

    x = int(x)
    row = (x - 1) // 3
    col = (x - 1) % 3

    if Board[row][col] != 0:
        if opponent or turn:
            print("Invalid Move")
        playMove()
        return
    else:
        if turn:
            Board[row][col] = 'X'
            turn = False
        else:
            Board[row][col] = 'O'
            turn = True


def game():
    global computerTurn
    moves()
    for i in range(9):
        printBoard(Board)
        playMove()
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
        turn = startingMove()
        computerTurn = False
        game()
    elif play == '2':
        opponent = False
        Board = initializeBoard()
        computerTurn = not firstMove()
        turn = startingMove()
        game()
    elif play == '0':
        break
    else:
        print("Invalid Input")
        continue
