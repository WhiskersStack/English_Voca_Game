""" Main module for the English vocabulary game. """
import time
from print_options import print_game_options
from loading_feature import loading
from create_game import create_game

def main():
    """
    Main function to start the English vocabulary game.
    """
    is_playing = True
    print("\nWelcome to the English Vocabulary Game!")
    loading()
    time.sleep(1)
    print("\nMain Menu:")
    while is_playing:
        print_game_options()
        choice = input("> Enter your choice (1/2/3/4) : ")
        if choice == "1":
            print("\n> Starting game...\n")
            time.sleep(1)
            create_game()
        elif choice == "2":
            print("\n> Starting edit mode...\n")
            time.sleep(1)
            # Call the edit mode function here
        elif choice == "3":
            print("\n> Showing options...\n")
            time.sleep(1)
        elif choice == "4":
            print("\n> Exiting the game...\n")
            time.sleep(1)
            is_playing = False
        else:
            print("\n> Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
