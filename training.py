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

    for u in words_list:
        for word in words_list[u]:
            word['counter'] = 0

    with open("x.json", "w", encoding="utf-8") as file:
        json.dump(words_list, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    load_words(1, "word1", "word2")
