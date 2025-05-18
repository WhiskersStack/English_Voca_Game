"""
Start the vocabulary training game
"""
import random


def play_the_game(word_list, word1, word2):
    """
    Play the vocabulary training game
    """
    is_playing = True
    flag = 0
    start = 0
    end = 0
    if word1:
        for word in word_list:
            if word1 == word['word'] or word2 == word['word']:
                flag += 1
                if flag == 1:
                    start = word_list.index(word)
                elif flag == 2:
                    end = word_list.index(word)

        if flag == 2:  # If both words are found
            word_range = end - start + 1
            while is_playing:  # Loop until the user decides to stop or all words are shown 7 times
                random_num = random.randint(start, end + 1)
                if word_list[random_num]['counter'] != 7:
                    print(f"\n> Word: {word_list[random_num]['word']}")
                    word_list[random_num]['counter'] += 1
                else:
                    word_range -= 1
                if word_range == 0:
                    print("\n> All words have been shown 7 times.\n")
                    is_playing = False
        else:
            print("\n> Words not found in the list.\n")
            return False

    print("\n> Exiting the game...\n")
