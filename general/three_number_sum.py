"""

<div class="_2jZTzmL4QeyFli2evn3qXg"><p>
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.
</p>
<p>
  If no three numbers sum up to the target sum, the function should return an
  empty array.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [12, 3, 1, 2, -6, 5, -8, 6]
<span class="CodeEditor-promptParameter">targetSum</span> = 0
</pre>
<h3>Sample Output</h3>
<pre>[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
</pre>
</div>

Try sorting the array and traversing it once. At each number, place a left pointer on the number
immediately to the right of your current number and a right pointer on the final number in the
array. Check if the current number, the left number, and the right number sum up to the target sum.
How can you proceed from there, remembering the fact that you sorted the array?

"""

def three_number_sum(array, target_sum):
    sorted_array = sorted(array)
    sorted_output_array = []
    current_index = 0
    left_index = 1
    right_index = len(sorted_array) - 1
    while current_index <= right_index and left_index <= right_index:
        current_value = sorted_array[current_index]
        left_value = sorted_array[left_index]
        right_value = sorted_array[right_index]

        tri_sum = current_value + left_value + right_value
        print(tri_sum)

        if tri_sum > target_sum:
            left_index += 1
        elif tri_sum < target_sum:
            right_index -= 1
        else:
            tri_array = [current_value, left_value, right_value]
            sorted_output_array.append(tri_array)




        #print(str(current_value) + " + ", str(left_value) + " + ", str(right_value) + " = ", str(tri_sum))
        current_index += 1









    # Write your code here.
    pass



if __name__ == '__main__':

    results = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    print(results)


