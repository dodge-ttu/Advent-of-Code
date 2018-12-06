import timeit
import operator
import re

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
        # print(a)
        if a:
            a = a[0]
            a_string = a_string.replace(a, "")
            # print(a_string)
            stop_mark = None
            ls = list(a_string)
        b = [i+j for itr,(i,j) in enumerate(zip(ls,ls[1:])) if (i.islower() & j.isupper()) & (i.lower()==j.lower())]
        # print(b)
        if b:
            b = b[0]
            a_string = a_string.replace(b, "")
            # print(a_string)
            stop_mark = None
            ls = list(a_string)
        if not a and not b:
            stop_mark = "STOP"

    return(len(a_string))

# def p1answer2(a_string):
#     stop_mark = None
#     ls = set(a_string)
#     while stop_mark == None:
#         a = None
#         b = None
#         a = [i+j for itr,(i,j) in enumerate(zip(ls,ls[1:])) if (i.isupper() & j.islower()) & (i.lower()==j.lower())]
#         # print(a)
#         if a:
#             a = a[0]
#             a_string = a_string.replace(a, "")
#             # print(a_string)
#             stop_mark = None
#             ls = list(a_string)
#         b = [i+j for itr,(i,j) in enumerate(zip(ls,ls[1:])) if (i.islower() & j.isupper()) & (i.lower()==j.lower())]
#         # print(b)
#         if b:
#             b = b[0]
#             a_string = a_string.replace(b, "")
#             # print(a_string)
#             stop_mark = None
#             ls = list(a_string)
#         if not a and not b:
#             stop_mark = "STOP"
#
#     return(len(a_string))



p1answers = {
    "p1answer1":p1answer1,
    # "p1answer2":p1answer2,
}

### Problem 1 tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 1] Test: PASS, Function: p1answer1 Input: dabAcCaCBAcCcaDA



####### Problem 2 #######

# One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should.
# Your goal is to figure out which unit type is causing the most problems, remove all instances of it
# (regardless of polarity), fully react the remaining polymer, and measure its length.

# For example, again using the polymer dabAcCaCBAcCcaDA from above:

# Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
# Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
# Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
# Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
# In this example, removing all C/c units was best, producing the answer 4.

### Test cases:

p2_a= ("dabAcCaCBAcCcaDA", 4)

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(original_string, testing=True):
    if testing:
        alphabet = ["a","b","c","d"]
    else:
        alphabet = [chr(96+i) for i in range(1,26)]
    clean_polymer_lengths = {}
    for letter in alphabet:
        a_string = original_string
        ls = list(a_string)
        stop_mark = None
        ls = [i for i in ls if i.lower() != letter]
        a_string = "".join(ls)
        a = None
        b = None
        while stop_mark == None:
            a = [i+j for itr,(i,j) in enumerate(zip(ls,ls[1:])) if (i.isupper() & j.islower()) & (i.lower()==j.lower())]
            # print(a)
            if a:
                a = a[0]
                a_string = a_string.replace(a, "")
                # print(a_string)
                stop_mark = None
                ls = list(a_string)
            b = [i+j for itr,(i,j) in enumerate(zip(ls,ls[1:])) if (i.islower() & j.isupper()) & (i.lower()==j.lower())]
            # print(b)
            if b:
                b = b[0]
                a_string = a_string.replace(b, "")
                # print(a_string)
                stop_mark = None
                ls = list(a_string)
            if not a and not b:
                stop_mark = "STOP"

        clean_polymer_lengths[letter] = len(a_string)

    shortest_polymer = min(clean_polymer_lengths.items(), key=operator.itemgetter(1))[1]

    return(shortest_polymer)

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

# [Problem 2] Test: PASS, Function: p2answer1 Input: dabAcCaCBAcCcaDA



####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_05_input.txt"

with open(file_path, "r") as my_file:
    data = my_file.read()

# Data was the same for problem one and two for this day.



####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1, testing=False):
    for (answer_name, answer) in answer_dict.items():
        if not testing:
            time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        else:
            time = timeit.timeit("{0}(data, testing=False)".format(answer_name), globals=globals(), number=loops)

        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1, testing=False)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Time: 2.18692 seconds on 1 loops, Function: p1answer1
# [Problem 2] Time: 8.15665 seconds on 1 loops, Function: p2answer1

# NOTE: Dictionary lookup

# max(dict.items(), key=operator.itemgetter(1))[0]