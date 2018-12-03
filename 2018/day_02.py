import timeit
import csv
import itertools
import re

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

def p1answer1(ls, II=0, III=0):
    for i in ls:
        i = sorted(i)
        groups = [list(group) for key, group in itertools.groupby(i)]
        two_letter = [True for i in groups if len(i) == 2]
        three_letter = [True for i in groups if len(i) == 3]
        if two_letter:
            II += 1
        if three_letter:
            III += 1

    return(II * III)

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

# [Problem 1] Test: PASS, Function: p1answer1 Input: ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']



####### Problem 2 #######

# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
#
# The IDs abcde and axcye are close, but they differ by two characters (the second and fourth)
# . However, the IDs fghij and fguij differ by exactly one character, the
# third (h and u). Those must be the correct boxes. What letters are common between
# the two correct box IDs? (In the example above, this is found by removing the differing
# character from either ID, producing fgij.


### Test cases:

p2_a = (["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"], "fgij")

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

# Fails on official data.
def p2answer1(ls):
    target_length = len(ls[0]) - 1
    # print(target_length)
    for pattern in ls:
        for match in ls:
            bb = []
            for letter in pattern:
                c = [m.start(0) for m in re.finditer(letter, match)]
                c = [match[i] for i in c]
                bb.extend(c)
            # print(bb, len(bb))
            if len(bb) == target_length:
                # print(bb)
                zz = "".join(bb)
                # print(zz)
                return(zz)

def p2answer2(ls):
    id_length = len(ls[0])
    # print(id_length)
    counts = []
    for pattern in ls:
        for match in ls:
            sums = [u==v for (u,v) in zip(pattern, match)]
            # print(sum(sums))
            counts.append((sums, pattern, sum(sums)))

    bb = [i[1] for i in counts if i[2] == id_length - 1]

    solution = ""
    for i in bb[0]:
        if i in [1]:
            solution = solution + i

    return(solution)

def p2answer3(ls):
    id_length = len(ls[0])
    # print(id_length)
    for (i,j) in itertools.combinations(ls, 2):
        a = [q == w for (q,w) in zip(i,j)]
        if sum(a) == id_length - 1:
            solution = "".join([z for z in i if z in j])
            return solution

p2answers = {
    "p2answer1":p2answer1,
    "p2answer2":p2answer2,
    "p2answer3":p2answer3,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 2] Test: PASS, Function: p2answer1 Input: ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
# [Problem 2] Test: FAIL, Function: p2answer2 Input: ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
# [Problem 2] Test: PASS, Function: p2answer3 Input: ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

####### Official Input Data #######

### Csv library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_02_input.txt"

with open(file_path, newline='') as csv_file:
    raw_data = csv.reader(csv_file, delimiter=" ")
    data = []
    for i in list(raw_data):
        data.extend(i)

# Data was the same for problem one and two for this day.



####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Time: 0.00438 seconds on 1 loops, Function: p1answer1
# [Problem 2] Time: 0.0013 seconds on 1 loops, Function: p2answer1
# [Problem 2] Time: 0.1725 seconds on 1 loops, Function: p2answer2
# [Problem 2] Time: 0.03807 seconds on 1 loops, Function: p2answer3



