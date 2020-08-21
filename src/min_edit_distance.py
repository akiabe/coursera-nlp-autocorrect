import numpy as np
import pandas as pd

import combine_edits

def min_edit_distance(source, target, ins_cost=1, del_cost=1, rep_cost=2):
    """
    :param source: a string corresponding to the string you are starting with
    :param target: a string corresponding to the string you want to end with
    :param ins_cost: an integer the insert cost
    :param del_cost: an integer the delete cost
    :param rep_cost: an integer the replace cost
    :return D: a matrix of len(source)+1 by len(target)+1 containing minimum edit distance
    :return med: the minimum edit distance(med) required to convert the source string to the target
    """
    # initialization of variable
    m = len(source)
    n = len(target)
    D = np.zeros((m+1, n+1), dtype=int)

    # fill in column 0, from row 1 to row m
    for row in range(1, m+1):
        D[row, 0] = D[row-1,0] + del_cost

    # fill in row 0, for all columns from 1 to n
    for col in range(1,n+1):
        D[0,col] = D[0,col-1] + ins_cost

    # loop through row 1 to column m
    for row in range(1,m+1):

        # loop through col 1 to column n
        for col in range(1,n+1):

            # initialize r_cost to the replace cost
            r_cost = rep_cost

            # check to see if source character at the previous row
            # matches the target character at the previous column
            if source[row-1] == target[col-1]:
                r_cost = 0

            # update the cost at row, col based on previous entries in the cost matrix
            D[row,col] = min([
                D[row-1,col] + del_cost,
                D[row,col-1] + ins_cost,
                D[row-1,col-1] + r_cost
            ])

    # set the minimun edit distance with the cost found at row m, column n
    med = D[m, n]

    return D, med


if __name__ == "__main__":
    print("---- test 1 ----")
    source = 'play'
    target = 'stay'

    matrix, min_edits = min_edit_distance(source, target)
    print("minimum edits: ",min_edits, "\n")

    idx = list('#' + source)
    cols = list('#' + target)
    df = pd.DataFrame(matrix, index=idx, columns=cols)
    print(df, "\n")

    print("---- test 2 ----")
    source = 'eer'
    target = 'near'

    matrix, min_edits = min_edit_distance(source, target)
    print("minimum edits: ",min_edits, "\n")

    idx = list('#' + source)
    cols = list('#' + target)
    df = pd.DataFrame(matrix, index=idx, columns=cols)
    print(df, "\n")

    print("---- test 3 ----")
    source = 'eer'
    targets = combine_edits.edit_two_letters(source, allow_switches=False)

    for t in targets:
        _, min_edits = min_edit_distance(source, t, ins_cost=1, del_cost=1, rep_cost=1)

        if min_edits != 2 and min_edits != 1:
            print(source, t, min_edits)