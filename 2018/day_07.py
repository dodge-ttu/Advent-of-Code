import timeit
import re

####### Problem 1 #######

# The instructions specify a series of steps and requirements about which steps must be finished before others
# can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the
# following instructions:
# 
# "Step C must be finished before step A can begin.
# "Step C must be finished before step F can begin.
# "Step A must be finished before step B can begin.
# "Step A must be finished before step D can begin.
# "Step B must be finished before step E can begin.
# "Step D must be finished before step E can begin.
# "Step F must be finished before step E can begin.
# 
# Visually, these requirements look like this:
# 
# 
#   -->A--->B--
#  /    \      \
# C      -->D----->E
#  \           /
#   ---->F-----
# 
# Your first goal is to determine the order in which the steps should be completed. If more than one step is
# ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:
# 
# Only C is available, and so it is done first.
# Next, both A and F are available. A is first alphabetically, so it is done next.
# Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
# After that, only D and F are available. E is not available because only some of its prerequisites are complete.
# Therefore, D is completed next.
# F is the only choice, so it is done next.
# Finally, E is completed.
# 
# "So, in this example, the correct order is CABDFE.

### Test cases:

p1_a = ([
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
    ], "CABDFE")

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

# Passes test case fails on official data. Crap answer
def p1answer1(ls, *args, **kwargs):
    order = ""
    counter = 0
    for instruction in ls:
        counter += 1
        words = re.split(" ", instruction)
        (one, two) = (words[1], words[7])
        if counter == 1:
            order = "{0}{1}".format(one,two)
        elif (one not in order) and (two not in order):
            order = "{0}{1}{2}".format(order,one,two)
        elif (two in order) and (one not in order):
            order = re.sub(two, "{0}{1}".format(one, two), order)
        # Sorting all after here ruins the order and is flawed logic
        else:
            ones_index = order.index(one)
            order = re.sub(one, "{0}{1}".format(one,two), order)
            order = "{0}{1}".format(order[:ones_index+1], "".join(sorted(order[ones_index+1:])))
            order = re.sub(r'(\w)\1', "", order)
    return(order)

# Ahhh... maybe...
def p1answer2(ls, *args, **kwargs):

    def build_instr_dict(ls, forward=True):

        if not forward:
            ls.reverse()

        parsed_instructions = []
        for instruction in ls:
            words = re.split(" ", instruction)
            (one,two) = words[1], words[7]

            if not forward:
                parsed_instructions.append((two, one))

            else:
                parsed_instructions.append((one,two))


        all_pieces = list(dict.fromkeys("".join([i+j for(i,j) in parsed_instructions])))

        instr_order = {k:[] for k in all_pieces}

        for (one,two) in parsed_instructions:
            instr_order[one].append(two)

        for (k,v) in instr_order.items():
            instr_order[k] = sorted(list(set(v)))

        return instr_order, all_pieces

    instr_order_forward, all_pieces = build_instr_dict(ls)
    instr_order_reversed, _ = build_instr_dict(ls, forward=False)

    prereqs_conditions = {}

    for value in instr_order_forward:
        prereqs_conditions[value] = [instr_order_reversed[value], instr_order_forward[value]]

    for (k,v) in prereqs_conditions.items():
        print(k,v)

    all_instructions = []

    for (k,v) in prereqs_conditions.items():
        temp = []
        if not v[0]:
            for j in v[1]:
                temp.append((k,j))
        elif not v[1]:
            for i in v[0]:
                temp.append((i, k))
        elif v[0] and v[1]:
            print(v[0], "else")
            (a,b) = v
            print(a)
            for i in a:
                temp.append((i, k))
            for j in b:
                temp.append((k, j))
        all_instructions.extend(temp)

    instruction_set = set(all_instructions)

    final_order = ""
    counter = 0
    length_all_pieces = len(all_pieces)

    while len(all_pieces) !=0:

        counter += 1

        num_before = []

        for piece in all_pieces:
            temp = []
            num_prereqs = len([i for i in instruction_set if i[1] == piece])
            if num_prereqs == 0:
                temp.extend(piece)
                num_before.extend(temp)

        num_before = sorted(num_before)

        print(num_before)

        order_temp = "".join(num_before)

        instruction_set = [i for i in instruction_set if i[0] not in num_before]

        for i in num_before:
            all_pieces.remove(i)

        final_order= final_order + order_temp

    print(final_order)

    return final_order

p1answers = {
    "p1answer1":p1answer1,
    "p1answer2":p1answer2,
}

### Problem 1 tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 1] Test: PASS, Function: p1answer1 Input: [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
# [Problem 1] Test: FAIL, Function: p1answer2 Input: [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]


####### Problem 2 #######


### Test cases:

p2_a = ([(1,1),(1,6),(8,3),(3,4),(5,5),(8,9)], 16)

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(ls, cutoff = 32, *args, **kwargs):
    pass

def p2answer2(*args, **kwargs):
    pass

p2answers = {
    "p2answer1":p2answer1,
    "p2answer2":p2answer2,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 2] Test: PA"S"S, Function: p2answer1 Input: []
# [Problem 2] Test: PA"S"S, Function: p2answer2 Input: []


####### Official Input Data #######

### C"SV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_07_input.txt"

with open(file_path) as my_file:
    data = my_file.read().splitlines()

# Data was the same for problem one and two for this day.


####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1, testing=False, *args, **kwargs):
    for (answer_name, answer) in answer_dict.items():
        if not testing:
            time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        else:
            time = timeit.timeit("{0}(data, testing=False)".format(answer_name), globals=globals(), number=loops)

        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)




