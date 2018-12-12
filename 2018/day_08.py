import timeit
import re

#region Problem 1
#
# The tree is made up of nodes; a single, outermost node forms the tree's root, and it contains all other nodes in
# the tree (or contains nodes that contain nodes, and so on).
#
# Specifically, a node consists of:
#
# A header, which is always exactly two numbers:
# The quantity of child nodes.
# The quantity of metadata entries.
# Zero or more child nodes (as specified in the header).
# One or more metadata entries (as specified in the header).
# Each child node is itself a node that has its own header, child nodes, and metadata. For example:
#
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----
# In this example, each node of the tree is also marked with an underline starting with a letter for easier
# identification. In it, there are four nodes:
#
# A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
# B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
# C, which has 1 child node (D) and 1 metadata entry (2).
# D, which has 0 child nodes and 1 metadata entry (99).

# The first check done on the license file is to simply add up all of the metadata entries. In this example,
# that sum is 1+1+2+10+11+12+2+99=138.
#
#endregion

### Test cases:

p1_a = ([2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2],138)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

def p1answer1(ls, *args, **kwargs):

    tree = {}
    node_ID = 0

    while ls:

        children = ls.pop(0)
        metadata = ls.pop(0)

        if children != 0:
            metas = []
            for i in range(metadata):
                metas.append(ls.pop(-1))
            tree[node_ID] = metas
            node_ID += 1
            print(metas)

        else:
            metas = []
            for i in range(metadata):
                metas.append(ls.pop(0))
            print(metas)

            tree[node_ID] = metas
            node_ID += 1

    all_sum = 0
    for (k,v) in tree.items():
        all_sum += sum(v)

    print(all_sum)

    return all_sum

    # # Recursive function to traverse dictionary.
    #
    # def open_dictionary(tree):
    #     for (k,v) in tree.items():
    #         if isinstance(v, dict):
    #             print("{0} : {1}".format(k, v))
    #             open_dictionary(v)


def p1answer2(*args, **kwargs):
    pass

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

#region Problem 2
#
#
#
#endregion

### Test cases:

p2_a = ([],0)

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(*args, **kwargs):
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



####### Official Input Data #######

### C"SV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_08_input.txt"

with open(file_path) as my_file:
    raw_data = my_file.read().split()
    data = []
    for i in raw_data:
        data.append(int(i))

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

