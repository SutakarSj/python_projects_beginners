import random

board=["-","-","-",
      "-","-","-",
      "-","-","-"]

currentplayer="X"
winner=None
gamerunning=True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
def playerinput(board):
    val=int(input("Enter value in range of(1-9) :"))
    if board[val-1]=="-":
        board[val-1]=currentplayer
    else:
        print("oops not valid")
        
def checkHori(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True

def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
def checkdiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True

def checkIfwin(board):
    global gamerunning
    if checkHori(board):
        printboard(board)
        print(f"The Winner is {winner}")
        gamerunning=False
    
    if checkrow(board):
        printboard(board)
        print(f"The Winner is {winner}")
        gamerunning=False
        
    elif checkdiag(board):
        printboard(board)
        print(f"The Winner is {winner}")
        gamerunning=False
        
def checkIftie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("The match is tie.")
        gamerunning=False
    
def switchplayer(): 
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    else:
        currentplayer="X"
    
    
def computerinput(board):
    global currentplayer
    while currentplayer=="O":
        place=random.randint(0, 8)
        if board[place]=="-":
            board[place]="O"
            switchplayer()
        
    
while gamerunning:
    printboard(board)
    playerinput(board)
    checkIfwin(board)
    checkIftie(board)
    switchplayer()
    computerinput(board)
    checkIfwin(board)
    checkIftie(board)