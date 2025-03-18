import random

Board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


turn = True  # Initialize turn variable
opponent = True  # Initialize opponent variable

def startingMove():
    global turn
    x = input("enter the starting move(X, O): ")
    x = x.upper()
    if x == 'X':
        turn = True
    elif x == 'O':
        turn = False
    else:
        print("Invalid Input")
        startingMove()



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



def computerMove():
    x = random.randint(1, 9)
    return x



def checkWin(Board):
    for i in range(3):
        if Board[i][0] == Board[i][1] == Board[i][2] != 0:
            printBoard(Board)
            print("Player", Board[i][0], "Wins")
            return True
        if Board[0][i] == Board[1][i] == Board[2][i] != 0:
            printBoard(Board)
            print("Player", Board[0][i], "Wins")
            return True
    if Board[0][0] == Board[1][1] == Board[2][2] != 0:
        printBoard(Board)
        print("Player", Board[0][0], "Wins")
        return True
    if Board[0][2] == Board[1][1] == Board[2][0] != 0:
        printBoard(Board)
        print("Player", Board[0][2], "Wins")
        return True
    return False

def checkMove(x):
    x = str(x)
    if x.isdigit() == False:
        return True
    
    x = int(x)
    if x < 1 or x > 9:
        return True
    else:
        return False
        

def playMove():
    global turn, opponent
    if not opponent and not turn:
        x = computerMove()
    else:
        print("Enter the number where you want to place your move (1-9):")
        x = input()

    if checkMove(x):
        print("Invalid Move")
        playMove()
        return
    
    x = int(x)
    row = (x - 1) // 3
    col = (x - 1) % 3
    
    if Board[row][col] != 0:
        if  opponent or turn:
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
    moves()
    for i in range(9):
        printBoard(Board)
        playMove()
        if checkWin(Board):
            return
    
    printBoard(Board)
    print("It's a tie")
    

while True:
    play = input("Do you want to play a game with a friend(1) or a computer(2) Eenter 0 to exit? ")
    if play == '1':
        opponent = True
        Board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        startingMove()
        game()
    elif play == '2':
        opponent = False
        Board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]  
        startingMove()
        game()
    elif play == '0':
        break
    else:
        print("Invalid Input")
        continue
