






def question_2(words, word1, word2):
    m = -1
    n = -1

    minimum = float('inf') # Max Integer value in python

    for i in range(len(words)):
        word = words[i]
        if word1 == word:
            m = i
            if n != -1:
                minimum = min(minimum, m-n)
        elif word2 == word:
            n = i
            if m != -1:
                minimum = min(minimum, n-m)


    return minimum if minimum != float('inf') else 0


if __name__ == '__main__':

    #results = question_2(['beaver', 'cat', 'fox', 'squirrel'], "beaver", "squirrel")
    results = question_2(['beaver', 'cat', 'fox'], "fox", "fox")
    print(results)

