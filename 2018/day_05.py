import timeit
import re
import csv
import datetime
from datetime import timedelta
from collections import Counter

####### Problem 1 #######

# The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of
# the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is
# represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas
# r and s are entirely different types and do not react.
#
# For example:
#
#  - In aA, a and A react, leaving nothing behind.
#  - In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
#  - In abAB, no two adjacent units are of the same type, and so nothing happens.
#  - In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.

# Now, consider a larger example, dabAcCaCBAcCcaDA:
#
# dabAcCaCBAcCcaDA  The first 'cC' is removed.
# dabAaCBAcCcaDA    This creates 'Aa', which is removed.
# dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
# dabCBAcaDA        No further actions can be taken.

### Test cases:

p1_a=("dabAcCaCBAcCcaDA" , 10)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

def p1answer1(a_string):
    stop_mark = None
    ls = list(a_string)
    while stop_mark == None:
        a = None
        b = None
        a = [i+j for itr,(i,j) in enumerate(zip(ls,ls[1:])) if (i.isupper() & j.islower()) & (i.lower()==j.lower())]
        print(a)
        if a:
            a = a[0]
            a_string = a_string.replace(a, "")
            print(a_string)
            stop_mark = None
            ls = list(a_string)
        b = [i+j for itr,(i,j) in enumerate(zip(ls,ls[1:])) if (i.islower() & j.isupper()) & (i.lower()==j.lower())]
        print(b)
        if b:
            b = b[0]
            a_string = a_string.replace(b, "")
            print(a_string)
            stop_mark = None
            ls = list(a_string)
        if not a and not b:
            stop_mark = "STOP"

    print(a_string)
    print(len(a_string))
    return(len(a_string))

p1answers = {
    "p1answer1":p1answer1,
}

### Problem 1 tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 1] Test: PASS, Function: p1answer1 Input: [[datetime.datetime(1518, 11, 1, 0, 0), ['Guard', '#10', 'begins', 'shift']], [datetime.datetime(1518, 11, 1, 0, 0, 5), ['falls', 'asleep']], [datetime.datetime(1518, 11, 1, 0, 0, 25), ['wakes', 'up']], [datetime.datetime(1518, 11, 1, 0, 0, 30), ['falls', 'asleep']], [datetime.datetime(1518, 11, 1, 0, 0, 55), ['wakes', 'up']], [datetime.datetime(1518, 11, 1, 23, 0, 58), ['Guard', '#99', 'begins', 'shift']], [datetime.datetime(1518, 11, 2, 0, 0, 40), ['falls', 'asleep']], [datetime.datetime(1518, 11, 2, 0, 0, 50), ['wakes', 'up']], [datetime.datetime(1518, 11, 3, 0, 0, 5), ['Guard', '#10', 'begins', 'shift']], [datetime.datetime(1518, 11, 3, 0, 0, 24), ['falls', 'asleep']], [datetime.datetime(1518, 11, 3, 0, 0, 29), ['wakes', 'up']], [datetime.datetime(1518, 11, 4, 0, 0, 2), ['Guard', '#99', 'begins', 'shift']], [datetime.datetime(1518, 11, 4, 0, 0, 36), ['falls', 'asleep']], [datetime.datetime(1518, 11, 4, 0, 0, 46), ['wakes', 'up']], [datetime.datetime(1518, 11, 5, 0, 0, 3), ['Guard', '#99', 'begins', 'shift']], [datetime.datetime(1518, 11, 5, 0, 0, 45), ['falls', 'asleep']], [datetime.datetime(1518, 11, 5, 0, 0, 55), ['wakes', 'up']]]



####### Problem 2 #######

# Exact same setup as above. When considering all guards, which minute is the guard who is most frequently
# asleep on the same minute?

### Test cases:

p2_a=

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(ls):

p2answers = {
    "p2answer1":p2answer1,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))




####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_05_input.txt"

with open(file_path, "r") as my_file:
    data = my_file.read()

# Data was the same for problem one and two for this day.



####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

