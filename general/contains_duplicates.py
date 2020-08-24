# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it
# should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true

# Example 2:

# Input: [1,2,3,4]
# Output: false

# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


# Method 1: Create a set of the nums array, convert back to a list,
# then compare the length of this set list with the length of the original nums list.
def contains_duplicates(nums):
  return True if len(list(set(nums))) != len(nums) else False

# Method 2: Using a dict / map iterate over numbers adding and checking for duplicate in the dict
def contains_duplicates_2(nums):
  container_dict = {}
  for num in nums:
    if num in container_dict:
      return True 
    else:
      container_dict[num] = True
  return False




