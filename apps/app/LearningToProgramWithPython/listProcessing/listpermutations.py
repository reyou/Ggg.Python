from random import *


def permute(prefix, suffix, sessionId):
    print("called sessionId", sessionId)
    print("called ", "prefix", prefix, "suffix", suffix, "sessionId", sessionId)
    sessionId = randrange(1, 10000)
    print("new sessionId", sessionId)
    '''
    Recursively shifts all the elements in suffix into
    prefix producing all the permutations of suffix.
    Prints all permutations in lexicographical order.
    :param prefix:
    :param suffix:
    :return:
    '''
    suffix_size = len(suffix)
    # Have we considered all the elements?
    if (suffix_size == 0):
        print("printing " + str(sessionId), prefix, end="\n\n")
        print("====================", end="\n\n")
    else:
        for i in range(0, suffix_size):
            print("for " + str(i) + " in range(0, " + str(suffix_size) + ")")
            print("original ", "prefix", prefix, "suffix", suffix, "sessionId", sessionId)
            new_pre = prefix + [suffix[i]]
            new_suff = suffix[:i] + suffix[i + 1:]
            print("calling sessionId", sessionId)
            print("calling ", "prefix", new_pre, "suffix", new_suff, "sessionId", sessionId)
            print("\n\n")
            permute(new_pre, new_suff, sessionId)


def print_permutations(lst):
    '''
    Calls the recursive permute function to display
    all the permutations of the elements of lst in
    lexicographical order. The empty list is passed as
    the first parameter to permute, and the list to
    permute is passed as the second argument.
    :param lst:
    :return:
    '''
    permute([], lst, "initialize")


def main():
    a = [1, 2, 3, 4]
    print_permutations(a)


main()
