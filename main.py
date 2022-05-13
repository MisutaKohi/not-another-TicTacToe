def print_board(dict):
    '''This function will be used to print the game board. It takes a
    dictionary that will represent the previous moves of the players.'''

def X_to_play(dictionary):
    '''This will represent X's turn. It will prompt the user to enter their
    move, and follow-up with additional instructions for proper formatting
    if needed.'''

def O_to_play(dictionary):
    '''This will represent O's turn. It will prompt the user to enter their
    move, and follow-up with additional instructions for proper formatting
    if needed.'''

def is_game_over(dictionary):
    '''This function will check to see if either team has achieved a 3 in a row.
    If so, the game will end. This function returns the name of the winning team
    or None if no winner has yet been determined.'''

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

        print('{}\'s are the winner! Congrats!')

        play_again = input('Would you like to play again? (y/n)' )

        if play_again[0].lower() == 'y':
            play_again = True
        else:
            play_again = False

    print('Thanks for playing!')

if __name__ == '__main__':
    main()
