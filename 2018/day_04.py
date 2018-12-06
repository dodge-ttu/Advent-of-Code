import timeit
import csv
import datetime
from datetime import timedelta
from collections import Counter

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
        # print(aa)
        i[0] = datetime.datetime.strptime(aa, "[%Y-%m-%d_%H:%S]")
        ls[itr] = [i[0], i[2:]]

    ls = sorted(ls, key=lambda x: x[0])
    ID_set = set([i[1][1] for i in ls if len(i[1]) == 4])
    group_ls = []
    for i in ls:
        if len(i[1]) == 4:
            temp = []
            ID_value = i[1][1]
            temp.append(i)
            group_ls.append((ID_value, temp))
        if len(i[1]) == 2:
            temp.append(i)

    # ttps://stackoverflow.com/a/1060330/7384740
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).seconds)):
            yield start_date + timedelta(seconds=n)

    sleep_ranges = []

    for (ID,i) in group_ls:
        start_sleeping = datetime.datetime(1500, 1, 1, 0, 0, 0)
        stop_sleeping = datetime.datetime(1500, 1, 1, 0, 0, 0)
        for j in i:
            if j[1][0] == "falls":
                start_sleeping = j[0]
            if j[1][0] == "wakes":
                stop_sleeping = j[0]
            if (start_sleeping < stop_sleeping):
                # print(ID, start_sleeping, stop_sleeping)
                seconds_sleeping = daterange(start_sleeping, stop_sleeping)
                sleep_ranges.append((ID, [i.second for i in seconds_sleeping]))

    all_minutes_each = []

    for ID in ID_set:
        chunk = [i for i in sleep_ranges if i[0] == ID]
        one_long = []
        for i in chunk:
            one_long.extend(i[1])
        all_minutes_each.append((ID, one_long))

    counts = []
    for ID, mins_sleeping in all_minutes_each:
        # print(ID)
        count_info = Counter(mins_sleeping).most_common(1)
        if count_info:
            most_common, _ = count_info[0]
        else:
            most_common = 0
        overall_mins = len(mins_sleeping)
        counts.append((ID, most_common, overall_mins))

    biggest_sleeper = max(counts, key=lambda x: x[2])

    answer = int(biggest_sleeper[0][1:]) * biggest_sleeper[1]

    return(answer)

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

# Exact same setup as above. For the guard who slept most, which minute did the most frequently sleep?

### Test cases:

p2_a= ([["[1518-11-01", "00:00]", "Guard", "#10", "begins", "shift"],
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
        ["[1518-11-05", "00:55]", "wakes", "up"]], 4455)

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(ls):
    for (itr,i) in enumerate(ls):
        aa = "{0}_{1}".format(i[0],i[1])
        # print(aa)
        i[0] = datetime.datetime.strptime(aa, "[%Y-%m-%d_%H:%S]")
        ls[itr] = [i[0], i[2:]]

    ls = sorted(ls, key=lambda x: x[0])
    ID_set = set([i[1][1] for i in ls if len(i[1]) == 4])
    group_ls = []
    for i in ls:
        if len(i[1]) == 4:
            temp = []
            ID_value = i[1][1]
            temp.append(i)
            group_ls.append((ID_value, temp))
        if len(i[1]) == 2:
            temp.append(i)

    # https://stackoverflow.com/a/1060330/7384740
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).seconds)):
            yield start_date + timedelta(seconds=n)

    sleep_ranges = []

    for (ID,i) in group_ls:
        start_sleeping = datetime.datetime(1500, 1, 1, 0, 0, 0)
        stop_sleeping = datetime.datetime(1500, 1, 1, 0, 0, 0)
        for j in i:
            if j[1][0] == "falls":
                start_sleeping = j[0]
            if j[1][0] == "wakes":
                stop_sleeping = j[0]
            if (start_sleeping < stop_sleeping):
                print(ID, start_sleeping, stop_sleeping)
                seconds_sleeping = daterange(start_sleeping, stop_sleeping)
                sleep_ranges.append((ID, [i.second for i in seconds_sleeping]))

    all_minutes_each = []

    for ID in ID_set:
        chunk = [i for i in sleep_ranges if i[0] == ID]
        one_long = []
        for i in chunk:
            one_long.extend(i[1])
        all_minutes_each.append((ID, one_long))

    counts = []
    for ID, mins_sleeping in all_minutes_each:
        # print(ID)
        count_info = Counter(mins_sleeping).most_common(1)
        if count_info:
            most_common, number_of = count_info[0]
        else:
            most_common, number_of = 0, 0
        # overall_mins = len(mins_sleeping)
        counts.append((ID, most_common, number_of))

    max_minute_slept = max(counts, key=lambda x: x[2])
    print(max_minute_slept)
    answer = int(max_minute_slept[0][1:]) * max_minute_slept[1]

    return(answer)


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

# [Problem 2] Test: PASS, Function: p2answer1 Input: [[datetime.datetime(1518, 11, 1, 0, 0), ['Guard', '#10', 'begins', 'shift']], [datetime.datetime(1518, 11, 1, 0, 0, 5), ['falls', 'asleep']], [datetime.datetime(1518, 11, 1, 0, 0, 25), ['wakes', 'up']], [datetime.datetime(1518, 11, 1, 0, 0, 30), ['falls', 'asleep']], [datetime.datetime(1518, 11, 1, 0, 0, 55), ['wakes', 'up']], [datetime.datetime(1518, 11, 1, 23, 0, 58), ['Guard', '#99', 'begins', 'shift']], [datetime.datetime(1518, 11, 2, 0, 0, 40), ['falls', 'asleep']], [datetime.datetime(1518, 11, 2, 0, 0, 50), ['wakes', 'up']], [datetime.datetime(1518, 11, 3, 0, 0, 5), ['Guard', '#10', 'begins', 'shift']], [datetime.datetime(1518, 11, 3, 0, 0, 24), ['falls', 'asleep']], [datetime.datetime(1518, 11, 3, 0, 0, 29), ['wakes', 'up']], [datetime.datetime(1518, 11, 4, 0, 0, 2), ['Guard', '#99', 'begins', 'shift']], [datetime.datetime(1518, 11, 4, 0, 0, 36), ['falls', 'asleep']], [datetime.datetime(1518, 11, 4, 0, 0, 46), ['wakes', 'up']], [datetime.datetime(1518, 11, 5, 0, 0, 3), ['Guard', '#99', 'begins', 'shift']], [datetime.datetime(1518, 11, 5, 0, 0, 45), ['falls', 'asleep']], [datetime.datetime(1518, 11, 5, 0, 0, 55), ['wakes', 'up']]]



####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_04_input.txt"

with open(file_path, newline='') as csv_file:
    raw_data = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in raw_data:
        data.append(row)

# Data was the same for problem one and two for this day.



####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Time: 0.01445 seconds on 1 loops, Function: p1answer1
# [Problem 2] Time: 0.01451 seconds on 1 loops, Function: p2answer1
