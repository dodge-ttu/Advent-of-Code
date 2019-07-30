import timeit
import csv
import pandas as pd
import numpy as np
import re

#region Problem 1
#
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from
# the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually,
# it claims the square inches of fabric represented by # (and ignores the square inches of
# fabric represented by .) in the diagram below:
#
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
#
# The problem is that many of the claims overlap, causing two or more claims to cover part
# of the same areas. For example, consider the following claims:
#
# 1 @ 1,3: 4x4
# 2 @ 3,1: 4x4
# 3 @ 5,5: 2x2
#
# Visually, these claim the following areas:
#
# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
#
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while
# adjacent to the others, does not overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough fabric.
# How many square inches of fabric are within two or more claims?
#
#endregion

### Test cases:

p1_a = ([["#1", "@", "1,3:", "4x4"],
         ["#2", "@", "3,1:", "4x4"],
         ["#3", "@", "5,5:", "2x2"]], 4)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

def p1answer1(ls):
    a = np.zeros((10000,10000))
    for i in ls:
        (ID, _, offset, size) = i
        from_left = int(re.findall(r"\d+", offset)[0])
        from_top = int(re.findall(r"\d+", offset)[1])
        rightward = int(re.findall(r"\d+", size)[0])
        downward = int(re.findall(r"\d+", size)[1])
        l_range = range(from_left, (from_left+rightward), 1)
        d_range = range(from_top, (from_top+downward), 1)
        for fl in l_range:
            for ft in d_range:
                # print(fl,ft)
                a[ft, fl] += 1
    x,y = np.where(a > 1)
    bb = x.tolist()
    cc = [i for i in bb]
    #print(cc)

    return(len(cc))

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

# [Problem 1] Test: PASS, Function: p1answer1 Input: [['#1', '@', '1,3:', '4x4'], ['#2', '@', '3,1:', '4x4'], ['#3', '@', '5,5:', '2x2']]

#region Problem 2
#
# Exact same setup as above but return the id of the item without any overlap.
#
#endregion

### Test cases:

p2_a = ([["#1", "@", "1,3:", "4x4"],
         ["#2", "@", "3,1:", "4x4"],
         ["#3", "@", "5,5:", "2x2"]], "#3")

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(ls):
    a = np.zeros((10000,10000))
    for i in ls:
        (ID, _, offset, size) = i
        from_left = int(re.findall(r"\d+", offset)[0])
        from_top = int(re.findall(r"\d+", offset)[1])
        rightward = int(re.findall(r"\d+", size)[0])
        downward = int(re.findall(r"\d+", size)[1])
        l_range = range(from_left, (from_left+rightward), 1)
        d_range = range(from_top, (from_top+downward), 1)
        for fl in l_range:
            for ft in d_range:
                a[ft, fl] += 1

    for i in ls:
        (ID, _, offset, size) = i
        from_left = int(re.findall(r"\d+", offset)[0])
        from_top = int(re.findall(r"\d+", offset)[1])
        rightward = int(re.findall(r"\d+", size)[0])
        downward = int(re.findall(r"\d+", size)[1])

        zz = a[from_top:from_top+downward,from_left:from_left+rightward]

        ww = zz == 1

        if False not in ww:
            # print(ID)

            return(ID)

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

# [Problem 2] Test: PASS, Function: p2answer1 Input: [['#1', '@', '1,3:', '4x4'], ['#2', '@', '3,1:', '4x4'], ['#3', '@', '5,5:', '2x2']]


####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_03_input.txt"

with open(file_path, newline='') as csv_file:
    raw_data = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in raw_data:
        data.append(row)

# Data was the same for problem one and two for this day.

### Pandas library

df = pd.read_csv(file_path, delim_whitespace=True, header=None)

####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Time: 0.48411 seconds on 1 loops, Function: p1answer1
# [Problem 2] Time: 0.17185 seconds on 1 loops, Function: p2answer1