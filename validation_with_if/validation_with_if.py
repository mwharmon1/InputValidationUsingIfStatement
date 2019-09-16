""" Author: Michael Harmon
    Last Date Modified: 09/09/2019
    Description: This program will prompt for user's name
    and 3 scores out of 100 then average the scores and
    display the name and average grade.
"""


def average():
    score1 = input('Enter 1st score out of 100: ')
    score2 = input('Enter 2nd score out of 100: ')
    score3 = input('Enter 3rd score out of 100: ')
    average_score = (int(score1) + int(score2) + int(score3)) / 3
    return average_score


if __name__ == '__main__':
    last_name = input('Enter your last name. ')
    first_name = input('Enter your first name. ')
    age = input('Enter your age. ')
    average_scores = average()
    print(last_name + ', ' + first_name + ' age ' + age + ' average grade: ' '% 5.2f' % average_scores)
