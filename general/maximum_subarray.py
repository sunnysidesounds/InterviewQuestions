1

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
# largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
# which is more subtle.

# Two Options:
# Start a new subarray
# Or extend the preivous subarray


def get_max_subarray(nums):
  max_so_far = float('-inf')
  max_ending_here = 0
  
  for i in range(len(nums)):
    extend_subarray = max_ending_here + nums[i]
    new_subarray = nums[i]
    max_ending_here = max(extend_subarray, new_subarray)
    max_so_far = max(max_so_far, max_ending_here)

  return max_so_far

def get_max_subarray_2(nums):
  subarray_max = 0
  max_at_point = 0

  for i in range(len(nums)): # iterate over our nums
    max_at_point = max_at_point + nums[i] # adding up our values   
    if max_at_point < 0: # set max_at_point to zero if less than zero
      max_at_point = 0      
    if subarray_max < max_at_point: # set subarray_max to the max_at_point when the subarray_max is less than max_at_point      
      subarray_max = max_at_point      

  return subarray_max

def get_max_subarray_3(array):

  max_so_far = 0
  max_ending_here = 0

  for i in range(len(array)):
    max_extend =  max_ending_here + array[i]
    new_subarray = array[i]
    max_ending_here = max(max_extend, new_subarray)
    max_so_far = max(max_so_far, max_ending_here)

  return max_so_far



if __name__ == '__main__':
  restuls = get_max_subarray([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
  print(restuls)