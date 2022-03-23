import pandas as pd
import random
import numpy as np
import json
import re


def trim_dictionary(words_list, word, feedback):
    """
    Trim words dictionary based on feedback from attempted wordle.
    """

    word_array = np.array([letter for letter in word])

    bad_letters = list(word_array[feedback == 0])
    good_letters = list(word_array[feedback == 1])
    excellent_letters = list(word_array[feedback == 2])

    # drop words that contain letters with feedback == 0
    for letter in bad_letters:
        words_list = [word for word in words_list if letter not in word]

    # drop words that DO NOT contain letters with feedback == 1 or == 2
    for letter in good_letters + excellent_letters:
        words_list = [word for word in words_list if letter in word]

    # drop words that contain letters with feedback == 1 in same position as attempted word
    for letter in good_letters:
        letter_location = np.where(word_array == letter)[0][0]
        words_list = [word for word in words_list if word[letter_location] != letter]

    # select from the remaining only words with letters with feedback == 2 in same position as attempted word
    for letter in excellent_letters:
        letter_location = np.where(word_array == letter)[0][0]
        words_list = [word for word in words_list if word[letter_location] == letter]

    return words_list


# importing txt file with five letters words

df = open('sgb-words.txt','r')
words_dictionary1 = df.read()



words_dictionary = re.sub("[^\w]", " ",  words_dictionary1).split()


# Terminal usage:run the script, use the first attempt word and then for the feedback type(for example): [0,1,2,0,1]. Based on the wordle result, where:
# 0 stands for letters which are not part of the correct word (black colored)
# 1 stands for letters which are part of the correct word, but in the wrong position (yellow colored)
# 2 stands for letters which are part of the correct word and in the correct position (green colored)



for attempt in range(6):
    # step 1: randomly choose a word
    word = random.choice(words_dictionary)
    print(f"Attempt {attempt+1} : {word}")

    # step 2: manually type the word in wordle

    # step 3: read user feedback from wordle 
    feedback_str = input("Please enter wordle feedback: ")
    feedback = np.array(json.loads(feedback_str))

    # step 4: update dictionary based on feedback
    words_dictionary = trim_dictionary(words_list=words_dictionary, 
                                       word=word,
                                       feedback=feedback)

                                    
