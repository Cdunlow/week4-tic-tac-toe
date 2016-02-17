#Charles Dunlow
#this is the layout of the board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])         
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])    #this will print out the board
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or #this will check across top row
            (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or #this will check across middle row
            (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or #this will check across bottom row
            (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or #this will check vertically on left row
            (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or #this will check vertically the middle row
            (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or #this will check vertically the right row
            (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or #this will check diagonally left to right
            (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))   #this will check diagonally right to left
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board)    #will print the board everytime
        print('Turn for ' + turn + '. Move on which space?')   #asks the user which move they want
        move = input()      #gets the answer the user inputed
        board[move] = turn  #places what the user said down
        if( checkWinner(board, 'X') ):            #cheaks to see if player x wins
            print('X wins!')               #prints x wins if they won
            break
        elif ( checkWinner(board, 'O') ):       #checks if o player wins
            print('O wins!')               #prints o wins if they won
            break
    
        if turn == 'X':                       #continues game if neither won
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
