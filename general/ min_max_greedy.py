import itertools


def min_max(k, arr):
    combinations = list(itertools.combinations(arr, k))
    minimized_unfairness = None
    for combination in combinations:

        unfairness = (max(combination) - min(combination))

        if unfairness == 0:
            return 0

        if not minimized_unfairness:
            minimized_unfairness = unfairness
        elif unfairness < minimized_unfairness:
            minimized_unfairness = unfairness

        mx = max(combination)
        mn = min(combination)

        print("max: {0}, min: {1} unfairness: {2}".format(mx, mn, unfairness))

    return minimized_unfairness

def min_max_2(k, arr):
    minimized_unfairness = None
    arr.sort()
    for i in range(len(arr) - k):
        unfairness = arr[i + k] - arr[i]
        if unfairness == 0:
            return 0
        if not minimized_unfairness:
            minimized_unfairness = unfairness
        elif unfairness < minimized_unfairness:
            minimized_unfairness = unfairness

        k-=1

    return minimized_unfairness




if __name__ == '__main__':
    #r1 = min_max(3, [10, 100, 300, 200, 1000, 20, 30])
    #print(r1)
#
    #r2 = min_max(2, [2, 1, 2, 1, 2, 1])
    #print(r2)

    var = [6327,
           571,
           6599,
           479,
           7897,
           9322,
           4518,
           571,
           6677,
           7432,
           815,
           6920,
           4329,
           4104,
           7775,
           5708,
           7991,
           5802,
           8619,
           6053,
           7539,
           7454,
           9000,
           3267,
           6343,
           7165,
           4095,
           439,
           5621,
           4095,
           153,
           1948,
           1018,
           6752,
           8779,
           5267,
           2426,
           9649,
           2190,
           9103,
           7081,
           3006,
           2376,
           7762,
           3462,
           151,
           3471,
           1453,
           2305,
           8442]


    r3 = min_max_2(8, var)
    print(r3)



