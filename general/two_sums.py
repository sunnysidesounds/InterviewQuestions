# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

# Method 1: Brute Force. O(n^2)
def find_two_sums(nums, target):
  for i in range(len(nums)):
    sum_item_one = nums[i]
    i += 1
    for j in range(len(nums) - 1):
      sum_item_two = nums[j+1]
      if (sum_item_one + sum_item_two) == target:
        return [i, j]
      j += 1

# Method 2: O(n) optimized version
def find_two_sums_2(nums, target):
  nums_to_index_dict = {} # define a dictionary / object / map
  index = 0 # define our first index
  # build a map of values to indexes: {2: 0, 7: 1, 11: 2, 15: 3}
  for num in nums:
    nums_to_index_dict[num] = index
    index += 1

  index_2 = 0
  #for item in nums: 
  for i in range(len(nums)):
    offset = (target - nums[i])
    if offset in nums_to_index_dict:
      return [index_2, nums_to_index_dict[offset]]

    index_2 += 1

  return []
    




      




