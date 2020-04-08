"""

  Given a non-empty string of lowercase letters and a non-negative integer
  representing a key, write a function that returns a new string obtained by
  shifting every letter in the input string by k positions in the alphabet,
  where k is the key.

  Note that letters should "wrap" around the alphabet; in other words, the
  letter <span>z</span> shifted by one returns the letter <span>a</span>.

Sample Input
 "xyz"
 2

Sample Output
"zab"




"""


def caesar_cipher_encryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dic = {}
    index = 0
    for letter in alphabet:
        alphabet_dic[letter] = index
        index += 1

    new_str = ""
    for char in string:
        index_location = alphabet_dic[char] + key
        if index_location >= 0 and index_location <= len(alphabet) - 1:
            new_str = new_str + alphabet[index_location]
        elif index_location > len(alphabet) - 1:
            new_index = abs(index_location - len(alphabet))
            if new_index > len(alphabet) - 1:
                new_index = abs(new_index - len(alphabet))

            new_str = new_str + alphabet[new_index]

    return new_str






    # Write your code here.
    pass


if __name__ == '__main__':

    tests =[
        {"string": "xyz", "key": 2, "expected": "zab"},
        {"string": "abc", "key": 0, "expected": "abc"},
        {"string": "xyz", "key": 5, "expected": "cde"},
        {"string": "abc", "key": 26, "expected": "abc"},
        {"string": "abc", "key": 57, "expected": "fgh"},
        {"string": "abc", "key": 52, "expected": "abc"},


    ]
    counter = 1
    for test in tests:
        results = caesar_cipher_encryptor(test['string'], test['key'])
        print("Test {0}".format(counter), results == test['expected'])
        print(results)

        counter += 1
