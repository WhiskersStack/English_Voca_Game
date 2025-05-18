"""
Updating the vocabulary file
"""

import json
import os
import time

def update_word(word, new_meaning, unit):
    """
    Check if the file exists
    """
    if not os.path.exists("vocabulary.json"):
        print("\n> Vocabulary file does not exist.\n")
        return

    # If it exists, read the existing words
    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)

    user_unit = "unit_" + str(unit)

    for w in words_list[user_unit]:
        if w["word"] == word.lower():
            w["meaning"] = new_meaning
            print("\n> Word updated successfully!\n")
            # Write the updated words back to the file
            with open("vocabulary.json", "w", encoding="utf-8") as file:
                json.dump(words_list, file, indent=4)
            return

    print("\n> Word not found in the vocabulary.\n")


def delete_word(word, unit):
    """
    Delete a word from the vocabulary
    """
    if not os.path.exists("vocabulary.json"):
        print("\n> Vocabulary file does not exist.\n")
        return

    with open("vocabulary.json", "r", encoding="utf-8") as file:
        words_list = json.load(file)

    user_unit = "unit_" + str(unit)

    for w in words_list[user_unit]:
        if w["word"] == word.lower():
            words_list[user_unit].remove(w)
            with open("vocabulary.json", "w", encoding="utf-8") as file:
                json.dump(words_list, file, indent=4)
                print("\n> Word deleted successfully!\n")
            print("\n> Word deleted successfully!\n")
            return

    print("\n> Word not found in the vocabulary.\n")


if __name__ == "__main__":
    # Example usage
    update_word("DDD", "a new dd", 1)
    time.sleep(2)
    delete_word("DDD", 1)
