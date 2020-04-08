"""
Imagine that you're a teacher who's just graded the final exam in a class.
You have a list of student scores on the final exam in a particular order
(not necessarily sorted), and you want to reward your students. You decide to
do so fairly by giving them arbitrary rewards following two rules:

- first, all students must receive at least one reward;

- second, any given student must receive strictly more rewards than an adjacent student (a student immediately
to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student
with a higher score.

Assume that all students
have different scores; in other words, the scores are all unique. Write a function
that takes in a list of scores and returns the minimum number of rewards that you
must give out to students, all the while satisfying the two rules.

Example :

Input: [8, 4, 2, 1, 3, 6, 7, 9, 5]
Output:[4, 3, 2, 1, 2, 3, 4, 5, 1] --> 25

- you're a teacher
- list of student scores on a final exam
- want to reward students.

two rules:
    first, all students must receive at least one reward
    second, any given student must receive strictly more rewards than an adjacent student

objective:
- function that takes in a list of scores and returns the minimum number of rewards that you
must give out to students, all the while satisfying the two rules

"""

def min_rewards(scores):
    scores_length = len(scores)
    rewards_list = [1] * scores_length

    # iterate from left to right
    for i in range(0, scores_length - 1):
        before_value = scores[i]
        current_value = scores[i + 1]
        if before_value > current_value:
            continue
        elif before_value < current_value:
            rewards_list[i + 1] = max(rewards_list[i + 1], rewards_list[i] + 1)

    # iterate from right to left
    for j in range(scores_length - 1, 0, -1):
        after_value = scores[j]
        current_value = scores[j - 1]
        if after_value > current_value:
            continue
        elif after_value < current_value:
            rewards_list[j - 1] = max(rewards_list[j - 1], rewards_list[j] + 1)
    return sum(rewards_list)
    pass



if __name__ == '__main__':

    tests = [
        {"input": [8, 4, 2, 1, 3, 6, 7, 9, 5], "output": 25},
        {"input": [1], "output": 1},
        {"input": [5, 10], "output": 3},
        {"input": [2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0], "output": 52},
        {"input": [2, 1, 4, 3, 6, 5, 8, 7, 10, 9], "output": 15},
        {"input": [0, 4, 2, 1, 3], "output": 9},
    ]

    counter = 1
    for test in tests:
        results = min_rewards(test['input'])
        print("TEST {0}".format(counter), results == test['output'])
        #print()

        counter += 1
