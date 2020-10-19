# Given an array of integers and an integer k, you need to find the total number of continuous subarrays
# whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2
# Input : arr[] = {10, 2, -2, -20, 10},
# k = -10
# Output : 3
# Subarrays: arr[0...3], arr[1...4], arr[3..4]
# have sum exactly equal to -10.
#
# Input : arr[] = {9, 4, 20, 3, 10, 5},
# k = 33
# Output : 2
# Subarrays : arr[0...2], arr[2...4] have sum
# exactly equal to 33.
#
#
# Constraints:
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# An efficient solution is while traversing the array, store sum so far in currsum. Also, maintain the count of
# different values of currsum in a map. If the value of currsum is equal to the desired sum at any instance
# increment count of subarrays by one. The value of currsum exceeds the desired sum by currsum – sum. If this
# value is removed from currsum then the desired sum can be obtained. From the map find the number of subarrays
# previously found having sum equal to currsum-sum. Excluding all those subarrays from the current subarray,
# gives new subarrays having the desired sum. So increase count by the number of such subarrays. Note that
# when currsum is equal to the desired sum then also check the number of subarrays previously having a sum
# equal to 0. Excluding those subarrays from the current subarray gives new subarrays having the desired sum.
# Increase count by the number of subarrays having sum 0 in that case.





def find_sum_k_integers(arr, k):

    # traversing the array
    # store sum so far in currsum
    # maintain the count of different values of currsum in a map.
    # if currsum is equal to k at any instance increment count of subarrays
    # if currsum > currsum – k
    # find in map the previously found sum equal to currsum - k
    # increase count by the number of such subarrays, excluding all those subarrays in the current subarray
    # currsum is equal to the desired sum, then also need to check the number of subarrays previously having a sum of 0

    current_sum = 0
    occurances = 0
    sums_so_far = {}

    for i in range(len(arr)):

        current_sum += arr[i]

        if current_sum == k:
            occurances += 1

        if current_sum - k in sums_so_far:
            occurances += sums_so_far[current_sum - k]

        if current_sum in sums_so_far:
            sums_so_far[current_sum] += 1
        else:
            sums_so_far[current_sum] = 1

    return occurances



if __name__ == '__main__':

    results = find_sum_k_integers([1, 1, 1], 2)
    print(results)
