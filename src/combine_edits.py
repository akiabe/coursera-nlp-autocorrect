from collections import Counter
import data_processing
import string_manipulation

def edit_one_letter(word, allow_switches=True):
    """
    :param word: the string/word for which we will generate all possible words that are one edit away
    :return edit_one_set: a set of words with one possible edit
    """
    # create set of words with one possible edit
    edit_one_set = set()

    # edit string by deleting letter
    edit_one_set.update(string_manipulation.delete_letter(word))

    # if allow_switches is true, edit string by switch letter
    if allow_switches:
        edit_one_set.update(string_manipulation.switch_letter(word))

    # edit string by replace letter
    edit_one_set.update(string_manipulation.replace_letter(word))

    # edit string by insert letter
    edit_one_set.update(string_manipulation.insert_letter(word))

    return edit_one_set


def edit_two_letters(word, allow_switches=True):
    """
    :param word: the input string/word
    :return edit_two_set: a set of strings with all possible two edits
    """
    # create set of words with two possible edit
    edit_two_set = set()

    # get a set of words with one possible edit
    edit_one_set = edit_one_letter(word, allow_switches)

    # loop through the set of words with one possible edit
    for w in edit_one_set:
        # if word is "w", get a set of words with one possible edit
        if w:
            edit_two = edit_one_letter(w, allow_switches)

            # update set of words with two possible edit
            edit_two_set.update(edit_two)

    return edit_two_set


def get_corrections(word, probs, vocab, n=2, verbose=False):
    """
    :param word: a user entered string to check for suggestions
    :param probs: a dictionary that maps each word to its probably in the corpus
    :param vocab: a set containing all vocabulary
    :param n: number of possible word corrections you want returned in the dictionary
    :return n_best: a list of tuples with the most probable n corrected word and their probabilities
    """
    # create empty list to store suggestion and probabilities
    suggestions = []
    n_best = []

    # generate suggestions for supplied word
    suggestions = (word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(vocab)

    # create best words dictionary which key is suggestion and value is the probability of word
    best_words = {s:probs.get(s, 0) for s in suggestions}

    # get highest values in a best_words dictionary
    n_best = Counter(best_words).most_common(n)

    #n_best = [[s, probs[s]] for s in list(reversed(suggestions))]

    if verbose: print("entered word =", word, "\nsuggestions =", suggestions)

    return n_best

if __name__ == "__main__":
    # load corpus data
    word_l = data_processing.process_data("../input/shakespeare.txt")

    # create set of corpus words
    vocab = set(word_l)

    # get word frequencies
    word_count_dict = data_processing.get_count(word_l)

    # get probability of word in the corpus
    probs = data_processing.get_prob(word_count_dict)

    my_word = 'dys'

    tmp_corrections = get_corrections(my_word, probs, vocab, 2, verbose=True)

    for i, word_prob in enumerate(tmp_corrections):
        print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")

    print(f"data type of corrections {type(tmp_corrections)}")


