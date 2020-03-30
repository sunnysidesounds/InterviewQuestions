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

    pass



if __name__ == '__main__':
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    results = min_rewards(scores)
    print(results)