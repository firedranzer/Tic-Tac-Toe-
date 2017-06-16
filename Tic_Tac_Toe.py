from __future__ import print_function
from IPython.display import clear_output
import random

#Printing Board
def display_board(board):
        clear_output()
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')


#Function to choose the marker for both player
def player_input():
    marker = ''
    while not (marker=='X' or marker == 'O'):
        marker=raw_input("Player 1:Do you wanna choose X or O?").upper()
    if marker=='X':
#returning tuples
        return('X','O')
    else:
        return('O','X')

#function to place the marker for the player at that position
def place_marker(board,marker,position):
    board[position] = marker
    
#function to check if the position on the board is empty
def check_board(board,position):
    return board[position] == ' '

#Function to check if any player has won
def win_check(board,marker):
    return ((board[1]==marker and board[2]==marker and board[3]==marker) or
    (board[4]==marker and board[5]==marker and board[6]==marker) or
    (board[7]==marker and board[8]==marker and board[9]==marker) or
    (board[1]==marker and board[4]==marker and board[7]==marker) or
    (board[2]==marker and board[5]==marker and board[8]==marker) or
    (board[3]==marker and board[6]==marker and board[9]==marker) or
    (board[1]==marker and board[5]==marker and board[9]==marker) or
    (board[3]==marker and board[5]==marker and board[7]==marker))

#Function to choose first player at random to start the game
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 1:'
    else:
        return 'Player 2:'

#Function to check for the board to be full
def full_board_check(board):
    for i in range(0,10):
        if check_board(board,i):
            return False
        return True

#Function to decide next player's move
def player_choice(board, position=None):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_board(board,int(position)):
        position = raw_input("Choose your next position (1-9) :")

    return int(position)

#Function to devide if the player wants to play again
def replay():
    return raw_input("Do you want to play again(yes or no)").lower().startswith('y')

#Main Function

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break








