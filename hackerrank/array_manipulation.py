"""

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is 10 after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be .


"""
import os


# O (n^2) - Not efficient enough
def array_manipulation(n, queries):
    permutated_array = [0] * (n + 1)
    for index, query in enumerate(queries, 1):
        sub_index = query[0]
        for i in range(query[0], query[1] + 1):
            permutated_array[sub_index] = permutated_array[sub_index] + query[2]
            sub_index += 1
        print(index, query, permutated_array[index])

    print(permutated_array)
    return max(permutated_array)

def array_manipulation_recursive(n, queries):
    return array_manipulation_recursive_helper(0, 0, queries, [0] * (n + 1))


def array_manipulation_recursive_helper(index, current_highest_value, operations_list, operation_results):
    if (len(operations_list)) == index:
        return current_highest_value
    else:
        query = operations_list[index]
        for i in range(query[0], query[1] + 1):
            operation_results[i] = operation_results[i] + query[2]
            if operation_results[i] > current_highest_value:
                current_highest_value = operation_results[i]
        index += 1
        print("highest_value ", current_highest_value, " - results ", operation_results)

        return array_manipulation_recursive_helper(index, current_highest_value, operations_list, operation_results)


def array_manipulation_opimize(n, queries):
    highest_value = 0
    result_value = 0
    opetaion_results = [0] * (n+1)
    for query in queries:
        a, b, k = [query[0], query[1], query[2]]
        opetaion_results[a-1] += k
        if b + 1 <= n:
            opetaion_results[b] -= k

    for result in opetaion_results:
        result_value += result
        highest_value = max(highest_value, result_value)

    return highest_value


if __name__ == '__main__':

    tests =[
        {"queries": [[1, 2, 100], [2, 5, 100], [3, 4, 100]], "n": 5, "expected": 200},
        {"queries": [[1, 5, 3], [4, 8, 7], [6, 9, 1]], "n": 10, "expected": 10},
        {"queries": [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]], "n": 10, "expected": 31},

    ]
    counter = 1
    for test in tests:

        results = array_manipulation_opimize(test['n'], test['queries'])
        print("Test {0}".format(counter), results == test['expected'])
        print("RESULTS: ", results)
        print()

        counter += 1


