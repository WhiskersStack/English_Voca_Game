"""This is a simple English vocabulary """
import time
from print_options import print_game_options


def main():
    """
    Main function to start the English vocabulary game.
    """
    print("\n\n\n Welcome to the English Vocabulary Game!\n\n\n")

    while True:
        print_game_options()
        choice = input("> Enter your choice (1/2/3/4/5) : ")

        if choice == "1":
            print("\n> Starting training mode...\n")
            time.sleep(1)
            # Call the training mode function here
        elif choice == "2":
            print("\n> Starting test mode...\n")
            time.sleep(1)
            # Call the test mode function here
        elif choice == "3":
            print("\n> Starting edit mode...\n")
            time.sleep(1)
            # Call the edit mode function here
        elif choice == "4":
            print("\n> Showing options...\n")
            time.sleep(1)
        elif choice == "5":
            print("\n> Exiting the game...\n")
            break
        else:
            print("\n> Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
