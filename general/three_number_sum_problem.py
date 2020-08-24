"""

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

  If no three numbers sum up to the target sum, the function should return an
  empty array.

<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [12, 3, 1, 2, -6, 5, -8, 6]

target = 0

12 + 3 + 6 = 21 high, move right pointer to the left
12 + 3 + -8  = 7


<span class="CodeEditor-promptParameter">targetSum</span> = 0
</pre>
<h3>Sample Output</h3>
<pre>[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
</pre>
</div>

<p class="_3nVuYIxRwVvifJRcbJqRO7">
Try sorting the array and traversing it once.
At each number, place a left pointer on the number
immediately to the right of your current number and
a right pointer on the final number in the array.

Check if the current number, the left number, and the
right number sum up to the target sum. How can you
proceed from there, remembering the fact that you sorted the array?
</p>


<p class="_3nVuYIxRwVvifJRcbJqRO7">
Since the array is now sorted
(see Hint #2), you know that moving the left pointer mentioned in
Hint #2 one place to the right will lead to a greater left number
and thus a greater sum. Similarly, you know that moving the right
pointer one place to the left will lead to a smaller right number
and thus a smaller sum. This means that, depending on the size of
each triplet's (current number, left number, right number) sum
relative to the target sum, you should either move the left pointer,
the right pointer, or both to obtain a potentially valid triplet.
</p>

"""
def three_number_sum(array, target_sum):

    sorted_array = sorted(array)

    triplet_sum_arr = []
    for current in range(0, len(sorted_array), +1):
        left = current + 1
        right = len(sorted_array) - 1
        current_value = sorted_array[current]

        while left < right:
            left_value = sorted_array[left]
            right_value = sorted_array[right]
            potential_sum = (current_value + left_value + right_value)
            if potential_sum == target_sum:
                triplet = [current_value, left_value, right_value]
                triplet_sum_arr.append(triplet)
                left += 1
                right -= 1
            elif potential_sum > target_sum:
                right -= 1
            elif potential_sum < target_sum:
                left += 1

    return triplet_sum_arr




if __name__ == "__main__":

    tests = [
        {"paramters": [[12, 3, 1, 2, -6, 5, -8, 6], 0], "expected": [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]},
    ]

    counter = 1
    for test in tests:
        results = three_number_sum(test['paramters'][0], test['paramters'][1])
        print("Test {0} n={1}".format(counter, test['paramters']), test['expected'] == results, results )

        counter += 1
    
    