"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: "012345"
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def longest_substring_without_duplication(string):

    last_seen = {}
    longest_sub_str = [0, 1]
    start_index = 0
    for index, char in enumerate(string):
        if char in last_seen:
            start_index = max(start_index, last_seen[char] + 1)
        if (longest_sub_str[1] - longest_sub_str[0]) < index + 1 - start_index:
            longest_sub_str = [start_index, index+1]
        last_seen[char] = index


    return string[longest_sub_str[0]:longest_sub_str[1]]




    #char_map = {}
    #index = 0
    #last_sub_string = ""
    #current_substring = ""
    #for char in string:
    #    if char not in char_map and char not in last_sub_string:
    #        char_map[char] = index
    #        current_substring = last_sub_string + char
    #        if len(current_substring) > len(last_sub_string):
    #            last_sub_string = current_substring
    #    else:
    #        index = max(index, char_map[char] + 1)
    #        current_substring = string[index]
    #        char_map = {}
    #        char_map[char] = index
#
    #    index += 1











if __name__ == '__main__':

    string = 'abcabcbb'
    results = longest_substring_without_duplication(string)
    print(results)