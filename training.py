"""
Vocabulary training game
"""

import json
import os
import random
from print_words import print_words


def load_words(unit, word1, word2):
    """
    Load words from the vocabulary file
    """
    if not os.path.exists("vocabulary.json"):
        print("\n> Vocabulary file does not exist.\n")
        return {}

    print_words()

    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)


if __name__ == "__main__":
    load_words(1, "word1", "word2")
