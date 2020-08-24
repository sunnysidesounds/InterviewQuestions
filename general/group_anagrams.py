"""
  Write a function that takes in an array of strings and groups anagrams together.

  Anagrams are strings made up of exactly the same letters, where order doesn't
  matter. For example, <span>"cinema"</span> and <span>"iceman"</span> are
  anagrams; similarly, <span>"foo"</span> and <span>"ofo"</span> are anagrams.

  Your function should return a list of anagram groups in no particular order.

    Sample Input
    words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
</pre>
<h3>Sample Output</h3>
<pre>[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]
</pre>
</div>


"""

def group_anagrams(words):
    anagram_map = {}
    # build a map of words
    for word in words:
        # sort the character, creating a word_key
        word_key = "".join(sorted(word))
        # If word key exists, add word_key and word to dict array
        if word_key in anagram_map:
            anagram_map[word_key].append(word)
        else:
            anagram_map[word_key] = [word]

    anagram_list = []
    # then build output of nested lists
    for key in anagram_map:
        anagram_list.append(anagram_map[key])

    return anagram_list

    pass



if __name__ == '__main__':

    tests = [
        {"input": ["yo", "act", "flop", "tac", "cat", "oy", "olfp"], "output": [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]},
        {"input": ["abc", "dabd", "bca", "cab", "ddba"], "output": [["abc", "bca", "cab"], ["dabd", "ddba"]]},
        {"input": ["abc", "cba", "bca"], "output": [["abc", "cba", "bca"]]},


    ]
    counter = 1
    for test in tests:
        results = group_anagrams(test['input'])
        print("Test {0} PASSED".format(counter), sorted(results) == sorted(test['output']))

        counter += 1

