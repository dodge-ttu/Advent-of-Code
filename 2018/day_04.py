import timeit
import csv
import pandas as pd
import numpy as np
import re
import datetime
import itertools

####### Problem 1 #######

# For example, consider the following records, which have already been organized into
# chronological order:

# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up

# Timestamps are written using year-month-day hour:minute format. The guard falling
# asleep or waking up is always the one whose shift most recently started. Because
# all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute
# portion (00 - 59) is relevant for those events.

# Visually, these records show that the guards are asleep at these times:

# Date   ID   Minute
#             000000000011111111112222222222333333333344444444445555555555
#             012345678901234567890123456789012345678901234567890123456789
# 11-01  #10  .....####################.....#########################.....
# 11-02  #99  ........................................##########..........
# 11-03  #10  ........................#####...............................
# 11-04  #99  ....................................##########..............
# 11-05  #99  .............................................##########.....

# The columns are Date, which shows the month-day portion of the relevant day; ID,
# which shows the guard on duty that day; and Minute, which shows the minutes during
# which the guard was asleep within the midnight hour. (The Minute column's header
# shows the minute's ten's digit in the first row and the one's digit in the
# second row.) Awake is shown as ., and asleep is shown as #.

# Note that guards count as asleep on the minute they fall asleep, and they count as
# awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25
# on 1518-11-01, minute 25 is marked as awake.

# If you can figure out the guard most likely to be asleep at a specific time, you
# might be able to trick that guard into working tonight so you can have the best
# chance of sneaking in. You have two strategies for choosing the best guard/minute
# combination.

# Strategy 1: Find the guard that has the most minutes asleep. What minute does that
# guard spend asleep the most?

# In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes
# (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10
# was asleep most during minute 24 (on two days, whereas any other minute the guard
# was asleep was only seen on one day).

# While this example listed the entries in chronological order, your entries are in
# the order you found them. You'll need to organize them before they can be analyzed.

# What is the ID of the guard you chose multiplied by the minute you chose? (In the
# above example, the answer would be 10 * 24 = 240.)

### Test cases:

p1_a= ([["[1518-11-01", "00:00]", "Guard", "#10", "begins", "shift"],
        ["[1518-11-01", "00:05]", "falls", "asleep"],
        ["[1518-11-01", "00:25]", "wakes", "up"],
        ["[1518-11-01", "00:30]", "falls", "asleep"],
        ["[1518-11-01", "00:55]", "wakes", "up"],
        ["[1518-11-01", "23:58]", "Guard", "#99", "begins", "shift"],
        ["[1518-11-02", "00:40]", "falls", "asleep"],
        ["[1518-11-02", "00:50]", "wakes", "up"],
        ["[1518-11-03", "00:05]", "Guard", "#10", "begins", "shift"],
        ["[1518-11-03", "00:24]", "falls", "asleep"],
        ["[1518-11-03", "00:29]", "wakes", "up"],
        ["[1518-11-04", "00:02]", "Guard", "#99", "begins", "shift"],
        ["[1518-11-04", "00:36]", "falls", "asleep"],
        ["[1518-11-04", "00:46]", "wakes", "up"],
        ["[1518-11-05", "00:03]", "Guard", "#99", "begins", "shift"],
        ["[1518-11-05", "00:45]", "falls", "asleep"],
        ["[1518-11-05", "00:55]", "wakes", "up"]], 240)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

def p1answer1(ls):

    for (itr,i) in enumerate(ls):
        aa = "{0}_{1}".format(i[0],i[1])
        i[0] = datetime.datetime.strptime(aa, "[%Y-%m-%d_%H:%S]")
        ls[itr] = [i[0], i[2:]]

    ls = sorted(ls, key=lambda x: x[0])

    def pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)

    one_to_the_next_shifts = pairwise(ls)

    shift_chunks = []
    for (one,next_one) in one_to_the_next_shifts:
        print("next :{0}".format(next_one[1][1][0]))
        if next_one[1][1][0] != "#":
            temp.append(one)
        shift_chunks.append(temp)

    # shift_log = {}
    # for i in ls:
    #     shift_log[i[0]] = i[1][1:]
    #
    # gaurd_IDs = []
    # for i in ls:
    #     if i[1][1][0] == "#":
    #         print(i[1][1])
    #         gaurd_IDs.append(i[1][1])
    #
    # shift_starts = []
    # for i in ls:
    #     if i[1][1][0] == "#":
    #         print(i)
    #         shift_starts.append(i)

    return(ls, gaurd_IDs, shift_starts, shift_log, shift_chunks)

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



####### Problem 2 #######

# Exact same setup as above but return the id of the item without any overlap.

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

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_04_input.txt"

with open(file_path, newline='') as csv_file:
    raw_data = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in raw_data:
        data.append(row)

# Data was the same for problem one and two for this day.

### Pandas library

df = pd.read_csv(file_path, sep="]", header=None)

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