import timeit
import csv
import itertools
import pandas as pd

####### Problem 1 #######

# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6

### Test cases:

p1_a = ([1,1,1], 3)
p1_b = ([1,1,-2], 0)
p1_c = ([-1,-2,-3], -6)

p1_test_cases = {
    "p1_a":p1_a,
    "p1_b":p1_b,
    "p1_c":p1_c,
}

### Answers:

def p1answer1(ls):
    return(sum(ls))

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

# [Problem 1] Test: PASS, Function: p1answer1 Input: [1, 1, 1]
# [Problem 1] Test: PASS, Function: p1answer1 Input: [1, 1, -2]
# [Problem 1] Test: PASS, Function: p1answer1 Input: [-1, -2, -3]



####### Problem 2 #######

# +1, -1 first reaches 0 twice.
# +3, +3, +4, -2, -4 first reaches 10 twice.
# -6, +3, +8, +5, -6 first reaches 5 twice.
# +7, +7, -2, -7, -4 first reaches 14 twice.

### Test cases:

p2_a = ([1, -1], 0)
p2_b = ([3, 3, 4, -2, -4], 10)
p2_c = ([-6, 3, 8, 5, -6], 5)
p2_d = ([7, 7, -2, -7, -4], 14)

p2_test_cases = {
    "p2_a":p2_a,
    "p2_b":p2_b,
    "p2_c":p2_c,
    "p2_d":p2_d,
}

### Answers:

def p2answer1(ls):
    ls = ls * 10000
    sums = [0]
    count = 0
    sum = 0
    while True:
        if (sum + ls[count]) in sums:
            return(sum + ls[count])
        else:
            sum += ls[count]
            count += 1
            sums.append(sum)
        # print(sum, ls[count])

def p2answer2(ls):
    sum = 0
    sums = []
    for i in itertools.cycle(ls):
        if (sum + i) in sums:
            return(sum + i)
        else:
            sum += i
            sums.append(sum)
        # print(sum, sums, i)

def p2answer3(ls):
    sum = 0
    sums = []
    for i in itertools.cycle(ls):
        if (sum + i) in sums:
            return(sum + i)
        else:
            sums.append(sum)
            sum += i
        # print(sum, sums, i)

def p2answer4(ls):
    sum = 0
    sums = {}
    for i in itertools.cycle(ls):
        if str(sum + i) in sums:
            return(sum + i)
        else:
            sums["{0}".format(sum)] = sum
            sum += i
        # print(sum, sums, i)

p2answers = {
    "p2answer1":p2answer1,
    "p2answer2":p2answer2,
    "p2answer3":p2answer3,
    "p2answer4":p2answer4,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 2] Test: PASS, Function: p2answer1 Input: [1, -1]
# [Problem 2] Test: PASS, Function: p2answer1 Input: [3, 3, 4, -2, -4]
# [Problem 2] Test: PASS, Function: p2answer1 Input: [-6, 3, 8, 5, -6]
# [Problem 2] Test: PASS, Function: p2answer1 Input: [7, 7, -2, -7, -4]
# [Problem 2] Test: FAIL, Function: p2answer2 Input: [1, -1]
# [Problem 2] Test: PASS, Function: p2answer2 Input: [3, 3, 4, -2, -4]
# [Problem 2] Test: PASS, Function: p2answer2 Input: [-6, 3, 8, 5, -6]
# [Problem 2] Test: PASS, Function: p2answer2 Input: [7, 7, -2, -7, -4]
# [Problem 2] Test: PASS, Function: p2answer3 Input: [1, -1]
# [Problem 2] Test: PASS, Function: p2answer3 Input: [3, 3, 4, -2, -4]
# [Problem 2] Test: PASS, Function: p2answer3 Input: [-6, 3, 8, 5, -6]
# [Problem 2] Test: PASS, Function: p2answer3 Input: [7, 7, -2, -7, -4]
# [Problem 2] Test: PASS, Function: p2answer4 Input: [1, -1]
# [Problem 2] Test: PASS, Function: p2answer4 Input: [3, 3, 4, -2, -4]
# [Problem 2] Test: PASS, Function: p2answer4 Input: [-6, 3, 8, 5, -6]
# [Problem 2] Test: PASS, Function: p2answer4 Input: [7, 7, -2, -7, -4]



####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_01_input.txt"

with open(file_path, newline='') as csv_file:
    raw_data = csv.reader(csv_file, delimiter=" ", quoting=csv.QUOTE_NONNUMERIC)
    data = []
    for i in list(raw_data):
        data.extend(i)

### Pandas library

df = pd.read_csv("/home/will/advent_of_code/Advent-of-Code/2018/day_01_input.txt", header=None)
data = list(df.loc[:, 0].values)

# Data was the same for problem one and two for this day.



####### Performance  #######

# Performance testing on official data.

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Time: 9e-05 seconds on 1 loops, Function: p1answer1
# [Problem 2] Time: 215.17744 seconds on 1 loops, Function: p2answer1
# [Problem 2] Time: 217.74534 seconds on 1 loops, Function: p2answer2
# [Problem 2] Time: 201.87448 seconds on 1 loops, Function: p2answer3
# [Problem 2] Time: 0.18462 seconds on 1 loops, Function: p2answer4

# NOTE: Sets are significantly faster for "lookup" operations!
# https://stackoverflow.com/a/17945009