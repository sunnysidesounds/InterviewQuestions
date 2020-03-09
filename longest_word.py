import re
# Longest Word
# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
# Examples
# Input: "fun&!! time"
# Output: time
# Input: "I love dogs"
# Output: love


# Method 1: O(n)
def longest_word(sentence):
  longest_word = ''
  longest_count = 0
  word_list = sentence.split(" ")
  for word in word_list:
    clean_word = re.sub('[^a-zA-Z0-9-_*.]', '', word)
    length_of_word = len(clean_word)
    if length_of_word > longest_count:
      longest_word = clean_word
      longest_count = length_of_word
  return longest_word
