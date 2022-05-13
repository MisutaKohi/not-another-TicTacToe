def print_board(dict):
    '''This function will be used to print the game board. It takes a
    dictionary that will represent the previous moves of the players.'''

def X_to_play(dictionary):
    ''''''

def O_to_play(dictionary):
    ''''''

def is_game_over(dictionary):
    ''''''

def main():

    game_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                  'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    winner = None

    while play_again = True:

        while True:

            X_to_play(game_board)

            winner = is_game_over(game_board)

            O_to_play(game_board)

            winner = is_game_over(game_board)

        print('{}\'s are the winner! Congrats!')

        play_again = input('Would you like to play again? (y/n)' )

        if play_again[0].lower() == 'y':
            play_again = True
        else:
            play_again = False

    print('Thanks for playing!')