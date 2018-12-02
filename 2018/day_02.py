import timeit
import csv
import itertools
import pandas as pd

####### Problem 1 #######

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
# Of these box IDs, four of them contain a letter which appears exactly
# twice, and three of them contain a letter which appears exactly three
# times. Multiplying these together produces a checksum of 4 * 3 = 12.

### Test cases:

p1_a = (["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"], 12)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

def p1answer1(ls):




    return(sum(ls))

p1answers = {
    "p1answer1":p1answer1,
}

### Tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))


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

### Tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))



# Problem 2, answer1(): ['PASS', 'PASS', 'PASS', 'PASS']
# Problem 2, answer2(): ['FAIL', 'PASS', 'PASS', 'PASS']
# Problem 2, answer3(): ['PASS', 'PASS', 'PASS', 'PASS']
# Problem 2, answer4(): ['PASS', 'PASS', 'PASS', 'PASS']




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

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)