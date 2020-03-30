"""
You are given two non-empty strings: a big string and a small string.
Write a function that returns the smallest substring in the big string that contains all of the characters
found in the small string. Note that
1) the substring can contain other characters not found in the small string,
2) the characters in the substring don't have to be in the same order as they appear in the small string, and
3) if the small string has duplicate characters, the substring has to contain those duplicate characters
(it can also contain more, but not fewer).


Sample input: "abcd$ef$axb$c$", "$$abf"
Sample output: "f$axb$"

With the two pointers mentioned in Hint #2,
move the right pointer to the right in the big string,
keeping track of all the characters you visit in a hash table
identical to the one mentioned in Hint #1, until you've
found all of the characters contained in the small string.
At that point, move the left pointer to the right in the big
string, keeping track of all the characters you "lose", and
stop once you no longer have all of the small string's characters
in between the left and right pointers. Then, repeat the process by moving
the right pointer forward and implementing the same logic described in this Hint.


"""


def smallest_substring_containing(big_string, small_string):

    current_smallest_substring = None
    small_string_map = {}
    for char in small_string:
        if char in small_string_map:
            small_string_map[char] = small_string_map[char] + 1
        else:
            small_string_map[char] = 1

    print(small_string_map)

    right = 0
    left = 0
    big_string_map = {}

    while left <= right:
        char = big_string[right]
        if char in small_string_map and char in big_string_map: # TODO : Need to not go over the counts.
            if big_string_map[char] < small_string_map[char]:
                big_string_map[char] = big_string_map[char] + 1

        elif char in small_string_map and char not in big_string_map:
            big_string_map[char] = 1

        # If both equals
        if small_string_map == big_string_map:
            matching_substring = big_string[left:right + 1]
            if not current_smallest_substring or len(matching_substring) < len(current_smallest_substring):
                current_smallest_substring = matching_substring

            print(current_smallest_substring)

            char = big_string[left]

            if char in big_string_map:
                big_string_map[char] = big_string_map[char] - 1
            left += 1

            print(big_string_map)
            print()

        else:
            if right < len(big_string) - 1:
                right += 1
            else:
                left += 1

    current_smallest_substring = '' if not current_smallest_substring else current_smallest_substring
    return current_smallest_substring
    pass




if __name__ == '__main__':
    #big = 'abcd$ef$axb$c$'
    big = 'a$fuu+afff+affaffa+a$Affab+a+a+$a$'



    #big = 'abcdefghijklmnopqrstuvwxyz'
    #small = '$$abf'
    #small = 'aajjttwwxxzz'
    small = 'a+$aaAaaaa$++'

    # Expected "affa+a$Affab+a+a+$a"

    results = smallest_substring_containing(big, small)
    print(results)