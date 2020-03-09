# Write a function to reverse a string

# Method 1 : O(n) Brute Force
def reverse_string_1(str):
    str_arr = list(str) # convert str to list
    i = len(str_arr) - 1 # get length of list
    new_reversed_str = "" # define a new reversed str
    while (i >= 0): # iterate backwards concatinating to the nely created new_reversed_str
        new_reversed_str += str_arr[i]
        i -= 1
    return new_reversed_str # return str reversed 


# Method 2 : (python way) : O(n) -- assuming
def reverse_string_2(str):
  # start at the last index and interate over backwards character by character.
  return str[::-1] 


# Method 3 : O(n)
def reverse_string_3(str):
  i = len(str) - 1 # get length of list
  new_reversed_str = "" # define a new reversed str
  while (i >= 0): # iterate backwards concatinating to the nely created new_reversed_str
    new_reversed_str += str[i]
    i -= 1
  return new_reversed_str # return str reversed   

