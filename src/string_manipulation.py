def delete_letter(word, verbose=False):
    """
    :param word: the string/word for which will generate all possible words
                 in the vocabulary which have 1 missing character
    :return delete_l: a list of all possible strings obtained by deleting 1 character from word
    """
    delete_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word))]
    delete_l = [L + R[1:] for L, R in split_l if R]

    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l


def switch_letter(word, verbose=False):
    """
    :param word: input string
    :return switches: a list of all possible strings with one adjacent character switched
    """
    switch_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word))]
    switch_l = [L + R[1:2] + R[0:1] + R[2:] for L, R in split_l if len(R) >= 2]

    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \nswitch_l = {switch_l}")

    return switch_l


def replace_letter(word, verbose=False):
    """
    :param word: the input string/word
    :return replace: a list of all possible strings that it replaced one letter from the original word
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word))]
    replace_l = [L + c + R[1:] for L, R in split_l if R for c in letters]

    # store to the set and remove a word from a list
    replace_set = set(replace_l)

    # remove a word in a set
    replace_set.discard(word)

    # turn the set back into a list and store it for easier viewing
    replace_l = sorted(list(replace_set))

    if verbose: print(f"input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")

    return replace_l


def insert_letter(word, verbose=False):
    """
    :param word: the input string/word
    :return inserts: a set of all possible strings with one new letter inserted at every offset
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    insert_l = [L + c + R for L, R in split_l for c in letters]

    if verbose: print(f"input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")

    return insert_l


if __name__ == "__main__":
    delete_word_l = delete_letter(word="cans", verbose=True)
    switch_word_l = switch_letter(word="eta", verbose=True)
    replace_l = replace_letter(word="can", verbose=True)
    insert_l = insert_letter(word='at', verbose=True)