import __future__ from print_function
from IPython.display import clear_output


player1_index=raw_input('Player 1 (X or O):')
if player1_index=='X':
    print 'Player 2 :{x}'.format(x='O')
    player2_index='O'
else:
    print 'Player 2 :{x}'.format(x='X')
    player2_index='X'
def board_input(player1_index,player2_index):
    for i in range(1,10,1):
        index[i]=input('What is your move(1-9):')
        if i%2==1:
            index[i]=player1_index
        else:
            index[i]=player2_index
        board


#Printing Board
def display_board(board):
    clear_output()
    print ('  |  |  ')
    print (' '+ index[7] +' | '+ index[8] +' | ' + index[9]+' ')
    print ('  |  |  ')
    print ('--------')
    print ('  |  |  ')
    print (' '+ index[7] +' | '+ index[8] +' | ' + index[9]+' ')
    print ('  |  |  ')
    print ('--------')
    print ('  |  |  ')
    print (' '+ index[7] +' | '+ index[8] +' | ' + index[9]+' ')
    print ('  |  |  ')


#Function to choose the marker for both player
def player_input():
    marker = ''
    while not (marker=='X' or marker == 'O'):
        marker=raw_input("Player 1:Do you wanna choose X or O?").upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
















