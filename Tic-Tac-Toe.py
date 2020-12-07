from os import system, name
from time import sleep
import random

# FUNCTION TO CLEAR OUTPUTS


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


#  FUNCTION THAT DISPLAYS GAME BOARD
def display_board(board):
    sleep(1)
    clear()

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# SAMPLE BOARD
test = ['$', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'X']


# TAKING PLAYERS INPUT AND ASSIGNING THEIR MARKERS I.E (X OR O)
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''

    while not marker == 'X' or marker == 'O':
        marker = input("Player1 : choose X or O").upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


# FUNCTION THAT TAKES A POSITION AND ASSIGN MARKER ON IT
def place_marker(board, marker, position):
    board[position] = marker


# WIN CHECK FUNCTION THAT RETURN TRUE IF WIN OTHERWISE FALSE
def win_check(board, mark):

    return (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark)


# FUNCTION DECIDE WHICH PLAYER GO FIRST (TOSS)
def choose_first():

    coin = random.randint(0, 1)

    if coin == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# FUNCTION TO CHECK TO SPACE IS AVAILABALE OR NOT (IS EMPTY OR NOT)


def space_check(board, position):
    return board[position] == ' '

# FUNCTION TO CHECK THE BOARD IS FULL OR NOT


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


# FUNCTION THAT ASKS FOR PLAYER'S NEXT POSTION
def player_choise(board):

    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or space_check(board, position):
        position = int(input("choose a position : (1-9)"))
        if(position in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
            return position

    return position


# FUNCTION TO ASKS THE PLAYERS THAT THEY WANT OT PLAY AGAIN..?
# def replay():

#     choise = input("Play again? Enter Yes or Not")

#     return choise == 'Yes'


# GAME PLAY
# WHILE TO KEEP RUNNING TO GAME
print("Welcome to TIC TAC TOE..!  [Created by Masud Ansari]")

while True:

    # PLAY THE GAME

    # SET EVERYTHING UP (BOARD,WHOSE FIRST, CHOOSE MARKER X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will play first')

    play_game = input('Ready to play? y or n?')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False


# THE GAME PLAY
    while game_on:
        if turn == 'Player 1':

            # PLAYER 1 TURN

            # display the board
            display_board(the_board)
            # choose a position
            position = player_choise(the_board)
            # place the marker on that position
            place_marker(the_board, player1_marker, position)

            # check if he won
            if win_check(the_board, player1_marker):

                display_board(the_board)
                print("PLAYER 1 HAS WON!!")
                game_on = False

             # or check if there is a tie
            else:

                if full_board_check(the_board):

                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on = False
                else:

                    turn = 'Player 2'
                    # No tir or No win? Then the next player's turn

        else:

            # PLAYER 2 TURN
            # display the board
            display_board(the_board)
            # choose a position
            position = player_choise(the_board)
            # place the marker on that position
            place_marker(the_board, player2_marker, position)

            # check if he won
            if win_check(the_board, player2_marker):

                display_board(the_board)
                print("PLAYER 2 HAS WON!!")
                game_on = False

             # or check if there is a tie
            else:

                if full_board_check(the_board):

                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on = False
                else:

                    turn = 'Player 1'
                    # No tir or No win? Then the next player's turn

   #     if not replay():
   #         break

    # BREAK OUT OF THE WHILE LOOP
