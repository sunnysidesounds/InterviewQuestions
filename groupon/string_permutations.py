from itertools import permutations


def permut_string(string, step = 0):
    if step == len(string):
        print("".join(string))

    for i in range(step, len(string)):
        string_copy = [c for c in string]
        # swap
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        permut_string(string_copy, step + 1)


def permit_string_2(string):
    return ["".join(p) for p in permutations(string)]