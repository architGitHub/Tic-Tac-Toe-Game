    
def display_board(board):
    """
    INPUT: board array
    OUTPUT: board structure
    """
    
    index = 1
    while index < len(board):
        if board[index] == '':
            board[index] = ' '
        index += 1
           
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('-----------------')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('-----------------')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    
def player_input():
    """
    INPUT:
    OUTPUT: X or O users in tuple
    """
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('What do you want (X or O) ? ')
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
def ask_player(marker):
    position = 0
    while True:
        try:
            position = int(input(f'Next position for Player ({marker}) ?: '))
            if position in range(1,10):
                return position
#               break
            else:
                print('Sorry, please input a number between 1-9')                
                continue
        except:
            print('Sorry, please input a number between 1-9')
        

def place_marker(board, marker, position):
    """
    INPUT: board array, marker(X or O), position
    OUTPUT:
    """
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))
    
def space_check(board, position):
    """
    TRUE means space available.
    """
    return board[position] == '' or board[position] == ' '

def full_board_check(board):
    """
    INPUT: board array
    OUTPUT: True if space available
    """
    flag = True
    for space in board:
        if space == '' or space == ' ':
            flag = False
            break
    return not flag

def replay():
    user_input = input('\nDo you want to play again? (Yes or No) \n')
    return user_input.lower() == 'yes' or user_input.lower() == 'y'


print('\n'*23)
print('========================')
print('Welcome to Tic Tac Toe!')
print('========================')

while True:
    board= ['#', '', '', '', '', '', '', '', '', '']
    display_board(board)
    first_marker, second_marker = player_input()
            
    #Player 1
    while True:
        if not full_board_check(board):
            print('\n')
            print('========================')
            print('Hard Luck..Nobody Won!')
            print('========================')
            break    
        position = ask_player(first_marker )
        #while position not in range(1,10):
          #  position = int(input(f'Next position for First Player ({first_marker}) ?: '))
        if space_check(board, position):
            place_marker(board, first_marker, position)
        else:
            print(f'----Position {position} occupied----')
            continue
        display_board(board)  
        if win_check(board, first_marker):
            print('\n====================================')
            print(f'Congratulations! ({first_marker}) Won')
            print('====================================')
            break
        
        #Player 2
        if not full_board_check(board):
            print('\n========================')
            print('DRAW !!..')
            print('========================')
            break   
        
        position = ask_player(second_marker )
        if space_check(board, position):
            place_marker(board, second_marker, position)
        else:
            print(f'----Position {position} occupied----')
            continue
        
        display_board(board)  
        if win_check(board, second_marker):
            print('\n====================================')
            print(f'Congratulations! ({second_marker}) Won')
            print('====================================')
            break
            
    if not replay():
        print('\n\nThank you for playing.')
        break