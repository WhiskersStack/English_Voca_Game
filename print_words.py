"""
Printing all the words
"""

import json
import os


def print_words():
    """
    Print all the words in the vocabulary
    """
    if not os.path.exists("vocabulary.json"):
        print("\n> Vocabulary file does not exist.\n")
        return

    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)

    for unit, words in words_list.items():
        print(f"\n{unit}:")
        for word in words:
            print(f"  - {word['word']}: {word['meaning']}")


if __name__ == "__main__":
    print_words()
