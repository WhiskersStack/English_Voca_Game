"""
Vocabulary training game
"""

import json
import os
from print_words import print_words
from play import play_the_game


def create_game():
    """
    Load words from the vocabulary file, and initialize the counter for each word.
    """
    if not os.path.exists("vocabulary.json"):
        print("\n> Vocabulary file does not exist.\n")
        return {}

    print_words()

    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)

    # Initialize the counter for each word
    for u in words_list:
        for word in words_list[u]:
            word['counter'] = 0

    play_unit = input("\n> Enter the unit you want to play (1/2/3...) : ")
    is_range = input("\n> Do you want to loop all the words? (y/n) : ").lower()

    if is_range == "y":
        word1 = int(input("\n> Enter the first word to start from : "))
        word2 = int(input("\n> Enter the last word to end : "))
        play_the_game(words_list, play_unit, word1, word2)
    else:
        play_the_game(words_list, play_unit, False, False)


if __name__ == "__main__":
    create_game()
