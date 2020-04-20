# Given an array nums, write a function to move all 0's to the end of it while maintaining #the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# Method 1:
def move_zeros_to_end(nums):  
  zeros = []
  for num in nums:
    if num == 0:
      zeros.append(num)
      nums.remove(num)
  return nums + zeros

# Method 2:
def move_zeros_to_end_2(nums):
  size = len(nums)
  counter = 0
  for i in range(size):
    if nums[i] != 0:
      nums[counter] = nums[i]
      counter += 1
  while counter < size: 
        nums[counter] = 0
        counter += 1

  return nums





