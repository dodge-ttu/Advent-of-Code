from aocd import get_data
import numpy as np
import timeit


data = get_data(day=12, year=2018)


##### PROBLEM 1 #####

### Test cases:
p1_a = (0,0)
p1_b = (0,0)

p1_test_cases = {
    "p1_a":p1_a,
    "p1_b":p1_b,
}

### Answers:
def p1answer1(x):
    pass


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


##### PROBLEM 2 #####

### Test Cases:
p2_a = (0,0)
p2_b = (0,0)

p2_test_cases = {
    'p1_a':p2_a,
    'p1_b':p2_b,
}

### Answers:
def p2answer1(x):
    pass


p2answers = {
    'p2answer1':p2answer1,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))


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
