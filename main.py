import reverse_string as rs
import merge_sorted_arrays as msa
import two_sums as ts
import maximum_subarray as ms
import move_zeros as mz
import contains_duplicates as cd
import rotate_array as ra
import longest_word as lw
import first_recurring_character as frc



# Reverse A String: 
#str = "Hi My name is Jason"
#print("Method 1: Reverse String --> {0}".format(rs.reverse_string_1(str)))
#print("Method 2: Reverse String --> {0}".format(rs.reverse_string_2(str)))
#print("Method 3: Reverse String --> {0}".format(rs.reverse_string_3(str)))


# Merge Sorted Arrays:
# arr1 = [1, 3, 4, 6, 7, 8]
# arr2 = [2, 3, 5, 9, 12, 15, 25, 99]
# Result should be: 
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 25, 99
# print("Method 1: Merge sorted array --> {0}".format(msa.merge_arrays(arr1, arr2)))
# print("Method 2: Merge sorted array --> {0}".format(msa.merge_arrays_2(arr1, arr2)))


# Two Sums: 
# #Given nums = [2, 7, 11, 15], target = 9,
# nums = [2, 7, 11, 15]
# target = 9
# print("Method 1: Two Sums --> {0}".format(ts.find_two_sums(nums, target)))
# print("Method 2: Two Sums --> {0}".format(ts.find_two_sums_2(nums, target)))

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


# Maximum SubArray: 
#max_nums = [-2,1,-3,4,-1,2,1,-5,4]
#print("Method 1: Max Subarray --> {0}".format(ms.get_max_subarray(max_nums)))
#print("Method 2: Max Subarray --> {0}".format(ms.get_max_subarray_2(max_nums)))


# Move Zeros
#zero_nums = [0,1,0,3,12]
#print("Method 1: Move Zeros --> {0}".format(mz.move_zeros_to_end(zero_nums)))
#print("Method 2: Move Zeros --> {0}".format(mz.move_zeros_to_end_2(zero_nums)))

# Contains Duplicate
nums = [1,2,3,1]
#nums = [1,2,3,4]
#nums = [1,1,1,3,3,4,3,2,4,2]
#print("Method 1: Contains Duplicates --> {0}".format(cd.contains_duplicates(nums)))

#print("Method 2: Contains Duplicates --> {0}".format(cd.contains_duplicates_2(nums)))


# Rotate Array
#nums = [1,2,3,4,5,6,7]
#nums = [-1,-100,3,99]
#k = 3
#print("Method 1: Rotate Array --> {0}".format(ra.rotate_array_k_steps(nums, k)))

# Longest Word
#sent = 'fun&!! time'
#print("Method 1: Longest Word --> {0}".format(lw.longest_word(sent)))

# First Recurring Characters

# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined
arr1 = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,4]
arr3 = [2,3,4,5]
arr4 = [2,5,5,2,3,5,1,2,4]

print("Method 1: First Recurring Characters --> {0}".format(frc.first_recurring_character(arr4)))



