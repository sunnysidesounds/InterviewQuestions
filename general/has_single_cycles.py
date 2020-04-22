"""

  You're given an array of integers where each integer represents a jump of its
  value in the array. For instance, the integer <span>2</span> represents a jump
  of two indices forward in the array; the integer <span>-3</span> represents a
  jump of three indices backward in the array.

  If a jump spills past the array's bounds, it wraps over to the other side. For
  instance, a jump of <span>-1</span> at index <span>0</span> brings us to the last index in
  the array. Similarly, a jump of <span>1</span> at the last index in the array brings us to
  index <span>0</span>.

  Write a function that returns a boolean representing whether the jumps in the
  array form a single cycle. A single cycle occurs if, starting at any index in
  the array and following the jumps, every element in the array is visited
  exactly once before landing back on the starting index.
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">array</span> = [2, 3, 1, -4, -4, 2]
</pre>
<h3>Sample Output</h3>
"""

def has_single_cycle(array):

    visited = [0] * len(array)
    if len(array) > 0:
        return _has_single_cycle(array, 0, visited)
    return False


def _has_single_cycle(array, current_index, visited):

    current_value = array[current_index]

    if 2 in visited:
        return False

    if current_index == 0 and all(v == 1 for v in visited):
        return True

    visited[current_index] = visited[current_index] + 1

    new_index = current_index + current_value

    if new_index >= 0 and new_index <= len(array) - 1:
        return _has_single_cycle(array, new_index, visited)
    else:
        if new_index < 0:
            cycle_index_to_end = len(array) + new_index
            #if cycle_index_to_end < 0:

            if cycle_index_to_end == -11:
                print()

            return _has_single_cycle(array, cycle_index_to_end, visited)
        elif new_index > len(array) - 1:
            cycle_index_to_begin = abs(len(array) - new_index)
            return _has_single_cycle(array, cycle_index_to_begin, visited)
        else:
            print()



    return False






    pass





if __name__ == '__main__':

    tests = [
        #{"data": [2, 3, 1, -4, -4, 2], "expected": True},
        #{"data": [1, -1, 1, -1], "expected": False},
        #{"data": [2, 2, -1], "expected": True},
        #{"data": [2, 2, 2], "expected": True},
        #{"data": [1, 1, 1, 1, 1], "expected": True},
        #{"data": [0, 1, 1, 1, 1], "expected": False},
        #{"data": [1, 1, 0, 1, 1], "expected": False},
        #{"data": [3, 5, 6, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2], "expected": True},
        #{"data": [3, 5, 5, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2], "expected": False},
        {"data": [10, 11, -6, -23, -2, 3, 88, 908, -26], "expected": True},
        #{"data": [10, 11, -6, -23, -2, 3, 88, 909, -26], "expected": False},



    ]
    counter = 1
    for test in tests:
        results = has_single_cycle(test['data'])
        print("Test {0} - PASSED : ".format(counter), results == test['expected'])

        counter += 1


