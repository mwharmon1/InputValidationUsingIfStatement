""" Author: Michael Harmon
    Last Date Modified: 09/15/2019
    Description: This program will prompt for user's name
    and 3 scores out of 100 then average the scores and
    display the name and average grade.
    Update: Added if in average() to check for negative input
"""


def average():
    score_1 = int(input('Enter 1st score out of 100: '))
    score_2 = int(input('Enter 2nd score out of 100: '))
    score_3 = int(input('Enter 3rd score out of 100: '))

    if score_1 <= 0 or score_2 <= 0 or score_3 <= 0:
        print("No negative scores please.")
        return -1
    else:
        average_score = (int(score_1) + int(score_2) + int(score_3)) / 3
        return average_score


if __name__ == '__main__':
    last_name = input('Enter your last name. ')
    first_name = input('Enter your first name. ')
    age = input('Enter your age. ')
    average_scores = average()
    print(last_name + ', ' + first_name + ' age ' + age + ' average grade: ' '% 5.2f' % average_scores)
