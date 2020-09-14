from django.shortcuts import render,redirect
# global variables
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# to print the winner at the end
winner = None

# To know the current player
current_player = "X"

game_still_going = True

# to refresh complete board and variable , to start a new game
def playagain(request):
    global winner,board,game_still_going,current_player
    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']

    winner = None

    current_player = "X"

    game_still_going = True
    return redirect('home')

# this function used to call three function
# which are checking winner and store the winner in  global variable 'winner'
def check_for_winner():
    row_winner = check_rows()

    column_winner = check_column()

    diagonal_winner = check_diagonal()
    global winner

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# this function checks a rows of board for winner
def check_rows():
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 | row2 | row3:
        global game_still_going
        game_still_going = None
        if row1:
            return board[0]
        elif row2:
            return board[3]
        elif row3:
            return board[6]


# this function checks a column of board for winner
def check_column():
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    if col1 | col2 | col3:
        global game_still_going
        game_still_going = False
        if col1:
            return board[0]
        elif col2:
            return board[1]
        elif col3:
            return board[2]

# this function checks a diagonal of board for winner, if anyone its return winner symbols
def check_diagonal():
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        global game_still_going
        game_still_going = False
        if diagonal1:
            return board[0]
        elif diagonal2:
            return board[2]


# this function checking match is tie or not
def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False

# to change a turn between two player
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


# this function handle turns between two players ,storing a value to display a board
def handle_turn(position):
    global  board
    board[position-1] = current_player
    flip_player()


# this function used to checks, If anyone win the match and check game tie or not
def check_if_game_over():
    check_for_winner()

    check_if_tie()


# this function to call handle turns and checking game still not ended
def playgame(request, pk):
    handle_turn(pk)
    check_if_game_over()
    return redirect('home')


# home page
def home(request):
    return render(request, 'base.html', {'board': board, 'winner': winner, 'player': current_player, 'game_still_going':game_still_going})




