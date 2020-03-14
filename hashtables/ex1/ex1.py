#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
    #                    hash_table_remove,
                        hash_table_retrieve)
    #                    hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Takes in weights list, length and limit and returns
    two weights that add up to the limit
    """
    # brute force solution
    #for i in range(len(weights)):
    #    for j in range(len(weights)):
    #        if weights[i] + weights[j] == limit and i > j:
    #            return (i, j)

    # now make use of a hash table:
    # we need to use insert to insert the weights values into the hashtable
    # insert takes in ht, key, value and retrieve has ht and key
    # if we want to implement limit - weights[i] we can use retrieve
    for i in range(length):
        check = hash_table_retrieve(ht, limit - weights[i])
        if check is not None:     # if we do find something from limit - weights
            answer = (i, check)   # we answer in the form of tuple
            return answer
        else:
            hash_table_insert(ht, weights[i], i)
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
