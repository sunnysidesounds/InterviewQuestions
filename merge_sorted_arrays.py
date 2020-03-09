
# Given 2 sorted arrays merge them into one array
# [1, 3, 4, 6, 7, 8], [2, 5, 9, 12, 15, 25, 99]



# Method 1 : 
def merge_arrays(arr1, arr2):  
  merged_list = (arr1 + arr2) # combine lists
  merged_list.sort() # used pythons built in to sort the list
  return merged_list # returnn the merged sorted list
    

# Method 2: 
def merge_arrays_2(arr1, arr2):
  arr1_length = len(arr1) # length of array 1 (list)
  arr2_length = len(arr2) # length of array 2 (list)
  combined_list = [None] * (arr1_length + arr2_length) # create a new array (list) the length of both array 1 and 2. 
  arr1_index = 0 # defined array 1 index
  arr2_index = 0 # define array 2 index
  combined_list_index = 0 # define combined list index

  while(arr1_index < arr1_length and arr2_index < arr2_length):
      # if both array 1 and 1 indexes are less than the length of array 1 and 2, iterate over the arrays
    
      # if the value of array 1 is less than the value in array 2, add array 1 value to combined list, adjust indexes for combined list and array 1
      if arr1[arr1_index] < arr2[arr2_index]:
        combined_list[combined_list_index] = arr1[arr1_index]
        combined_list_index += 1
        arr1_index += 1
      else: # add array 2 value to the combined list, adjust index for combined and array 2
        combined_list[combined_list_index] = arr2[arr2_index]
        combined_list_index += 1
        arr2_index += 1

  # iterate over the remaining values in array 1, add to the combined list
  while(arr1_index < arr1_length):
    combined_list[combined_list_index] = arr1[arr1_index]
    combined_list_index += 1
    arr1_index += 1

  # iterate over the remaining values in array 2, add to the combined list
  while(arr2_index < arr2_length):
    combined_list[combined_list_index] = arr2[arr2_index]
    combined_list_index += 1
    arr2_index += 1

  return combined_list # return merged sorted list








  






