import csv
import itertools
import pandas as pd

####### Problem 1 #######

# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6

### Test cases:

a = ([1,1,1], 3)
b = ([1,1,-2], 0)
c = ([-1,-2,-3], -6)

test_cases = [a,b,c]

### Answers:

def answer1(ls):
    return(sum(ls))

answers = [answer1]

### Tests:

for itr, answer in enumerate(answers):
    test_results = ["PASS" if (answer(test) == sol) else "FAIL" for test, sol in test_cases]
    print("Problem 1, answer{0}(): {1}".format(itr+1, test_results))

# Problem 1, answer1(): ['PASS', 'PASS', 'PASS']



####### Problem 2 #######

# +1, -1 first reaches 0 twice.
# +3, +3, +4, -2, -4 first reaches 10 twice.
# -6, +3, +8, +5, -6 first reaches 5 twice.
# +7, +7, -2, -7, -4 first reaches 14 twice.

### Test cases:

a = ([1, -1], 0)
b = ([3, 3, 4, -2, -4], 10)
c = ([-6, 3, 8, 5, -6], 5)
d = ([7, 7, -2, -7, -4], 14)

test_cases = [a,b,c,d]

### Answers:

def answer1(ls):
    ls = ls * 100000
    sums = [0]
    count = 0
    sum = 0
    while True:
        if (sum + ls[count]) in sums:
            # print(sum + ls[count])
            return(sum + ls[count])
        else:
            # print(sum, ls[count])
            sum += ls[count]
            count += 1
            sums.append(sum)


def answer2(ls):
    sum = 0
    sums = []
    for i in itertools.cycle(ls):
        if (sum + i) in sums:
            # print(sum + i)
            return(sum + i)
        else:
            # print(sum, sums, i)
            sum += i
            sums.append(sum)


answers = [answer1, answer2]

### Tests:

for itr, answer in enumerate(answers):
    test_results = ["PASS" if (answer(test) == sol) else "FAIL" for test, sol in test_cases]
    print("Problem 2, answer{0}(): {1}".format(itr+1, test_results))

# Problem 2, answer1(): ['PASS', 'PASS', 'PASS', 'PASS']
# Problem 2, answer2(): ['FAIL', 'PASS', 'PASS', 'PASS']



####### Official Input Data #######

### Csv library

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

