def print_board(dictionary):
    '''This function will be used to print the game board. It takes a
    dictionary that will represent the previous moves of the players
    and format them to fit the game board.'''

    print('      L  M  R ')
    print('top  ' + dictionary['top-L'] + ' | ' + dictionary['top-M'] + ' | '+ dictionary['top-R'])
    print('     --+---+--')
    print('mid  ' + dictionary['mid-L'] + ' | ' + dictionary['mid-M'] + ' | '+ dictionary['mid-R'])
    print('     --+---+--')
    print('low  '+dictionary['low-L'] + ' | ' + dictionary['low-M'] + ' | ' + dictionary['low-R'])

def X_to_play(dictionary):
    '''This will represent X's turn. It will prompt the user to enter their
    move, and follow-up with additional instructions for proper formatting
    if needed.'''

    proper_moves = dictionary.keys()

    while True:
        player_move = input("Please enter your move (X): ")

        if player_move not in proper_moves:
            print('Please enter a row and column. For example, \'low-R\' or \'mid-M\' with this formatting.')
            continue

        if dictionary.get(player_move) != ' ':
            print("That square is already taken. Please enter a different one.")
        else:
            dictionary[player_move] = 'X'
            break


def O_to_play(dictionary):
    '''This will represent O's turn. It will prompt the user to enter their
    move, and follow-up with additional instructions for proper formatting
    if needed.'''

    proper_moves = dictionary.keys()

    while True:
        player_move = input("Please enter your move (O): ")

        if player_move not in proper_moves:
            print('Please enter a row and column. For example, \'low-R\' or \'mid-M\' with this formatting.')
            continue

        if dictionary.get(player_move) != ' ':
            print("That square is already taken. Please enter a different one.")
        else:
            dictionary[player_move] = 'O'
            break

def is_game_over(dictionary):
    '''This function will check to see if either team has achieved a 3 in a row.
    If so, the game will end. This function returns the name of the winning team
    or None if no winner has yet been determined.'''

    squares = list(dictionary.values())

    horizontal_wins = str(squares[0] + squares[1] + squares[2]) + ' ' + str(squares[3] + squares[4] + squares[5]) + \
                      ' ' + str(squares[6] + squares[7] + squares[8])

    vertical_wins = str(squares[0] + squares[3] + squares[6]) + ' ' + str(squares[1] + squares[4] + squares[7]) + \
                    ' ' + str(squares[2] + squares[5] + squares[8])

    diagonal_wins = str(squares[0] + squares[4] + squares[8]) + ' ' + str(squares[2] + squares[4] + squares[6])

    if 'XXX' in horizontal_wins:
        return 'X'
    elif 'XXX' in vertical_wins:
        return 'X'
    elif 'XXX' in diagonal_wins:
        return 'X'
    elif 'OOO' in horizontal_wins:
        return 'O'
    elif 'OOO' in vertical_wins:
        return 'O'
    elif 'OOO' in diagonal_wins:
        return 'O'

    count = 0
    for value in squares:
        if value != ' ':
            count += 1
    if count == 9:
        return 'Tie'

    return None



def main():
    '''This is the main function and entry point to this program.'''

    game_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                  'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    winner = None

    while play_again:

        while True:

            X_to_play(game_board)

            winner = is_game_over(game_board)

            if winner != None:
                break

            O_to_play(game_board)

            winner = is_game_over(game_board)

            if winner != None:
                break

        if winner == 'Tie':
            print('Cat\'s game! Tie all.')
        else:
            print('{}\'s are the winner! Congrats!'.format(winner))

        play_again = input('Would you like to play again? (y/n)' )

        if play_again[0].lower() == 'y':
            play_again = True
        else:
            play_again = False

    print('Thanks for playing!')

if __name__ == '__main__':

    dictionary = {'top-L': 'X', 'top-M': 'X', 'top-R': 'O',
                  'mid-L': 'O', 'mid-M': 'O', 'mid-R': 'X',
                  'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    print(is_game_over(dictionary))
