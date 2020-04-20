"""

Write a function that takes in a big string and an array of small strings,
all of which are smaller in length than the big string. The function should
return an array of booleans, where each boolean represents whether the small
string at that index in the array of small strings is contained in the big
string.

Note that you can't use language-built-in string-matching methods.

Sample Input
              0   1  2  3    4
bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]

Sample Output
[true, false, true, true, false, true, false]

"""

def multi_string_search_2(big_string, small_string):
    final_output = [False] * len(small_string)

    big_string_array = []
    current_str = ""
    index = 0
    for char in big_string:
        if char == " ":
            big_string_array.append(current_str)
            current_str = ""
        elif index == len(big_string) - 1:
            current_str = current_str + char
            big_string_array.append(current_str)
            current_str = ""
        else:
            current_str = current_str + char
        index += 1

    print(big_string_array)
    for i in range(len(small_string)):
        char = small_string[i]
        if char in big_string_array:
            final_output[i] = True

    return final_output


def multi_string_search(big_string, small_string):
    small_string_trie = Trie()
    for word in small_string:
        small_string_trie.add(word)

    words_trie = small_string_trie.root
    word_list = big_string.split(' ')


    current_word_list = [False] * len(small_string)
    for word in word_list:
        first_letter_in_word = word[0]
        if first_letter_in_word in words_trie:
            word_node = words_trie[first_letter_in_word]
            for i in range(1, len(word)):
                letter = word[i]
                if letter in word_node:
                    word_node = word_node[letter]
                    if '*' in word_node:
                        current_word_list
                else:
                    print()


    return current_word_list

    pass



class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word


if __name__ == '__main__':
    tests =[
        {"big": "this is a big string", "small": ["this", "yo", "is", "a", "bigger", "string", "kappa"],
         "expected": [True, False, True, True, False, True, False]},
        {"big": "Mary goes to the shopping center every week.", "small": ["to", "Mary", "centers", "shop", "shopping", "string", "kappa"],
         "expected": [True, True, False, True, True, False, False]}
    ]
    counter = 1
    for test in tests:
        results = multi_string_search(test['big'], test['small'])
        print("Test {0}".format(counter), results == test['expected'])
        print(results)

        counter += 1

