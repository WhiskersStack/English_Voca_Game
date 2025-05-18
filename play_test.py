""" Start the vocabulary test game. """
import time
from print_words import print_words

def start_test(word_list):
    """
    Start the vocabulary test game.
    """
    unit = input("\n> Enter the unit you want to test on (1/2/3...) : ")
    is_unit = print_words(unit)
    i = 1
    correct_answers = 0
    incorrect_answers = 0
    if is_unit:
        print("\n> Starting the test...\n")
        for word in word_list[unit]:
            print(f"{i}. {word['word']}")
            answer = input("\n> Enter answer : ")
            if answer == word['meaning']:
                print("\n> Correct!\n")
                correct_answers += 1
            else:
                print(f"\n> Incorrect! The correct answer is: {word['meaning']}\n")
                incorrect_answers += 1
            i += 1
            print("\n> Next word...\n")
            time.sleep(1.5)  # Wait for 1.5 seconds
