import re
from collections import Counter
import numpy as np
import pandas as pd

def process_data(file_name):
    """
    :param file_name: a file name which is found in current directory
    :return words: a list containing all the words in the corpus in lower case
    """
    words = []

    # read a file
    with open(file_name, 'r') as f:
        # read all content of text file
        file_name_data = f.read()

        # change all strings to lowercase
        change_data_to_lowercase = file_name_data.lower()

        # get match strings, any lowercase english, and pass to list
        words = re.findall(r'\w+', change_data_to_lowercase)

    return words


def get_count(word_l):
    """
    :param word_l: a set of words representing the corpus
    :return word_count_dict: the word dictionary where key is the word and value is its frequency
    """
    word_count_dict = {}

    # loop through the words corpus
    for word in word_l:

        # if word in word dictionary
        if word in word_count_dict:

            # add one to word dictionary at key "word"
            word_count_dict[word] += 1

        # else, set one to word dictionary at key "word"
        else:
            word_count_dict[word] = 1

    return word_count_dict


def get_prob(word_count_dict):
    """
    :param word_count_dict: the wordcount dictionary where key is the word and value is its frequency
    :return probs: a dictionary where keys are the words and the values are the probability that a word will occur
    """
    probs = {}

    # loop through the word dictionary by keys
    for word in word_count_dict.keys():
        # total number of words in the corpus
        total_number_of_words = sum(word_count_dict.values())

        # total number of times "word" appears in the corpus
        total_number_of_times_word_appears = word_count_dict.get(word, 0)

        # probability of "word" in the corpus
        probs[word] = total_number_of_times_word_appears / total_number_of_words

    return probs


if __name__ == "__main__":
    # load corpus data
    word_l = process_data("../input/shakespeare.txt")

    # create set of corpus words
    vocab = set(word_l)
    print(word_l[0:5])
    print(len(vocab))

    # get word frequencies
    word_count_dict = get_count(word_l)
    print(len(word_count_dict))
    print(word_count_dict.get('muse',0))

    # get probability of word in the corpus
    probs = get_prob(word_count_dict)
    print(len(probs))
    print(probs['thee'])