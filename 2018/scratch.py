import timeit

####### working scenario #######

test1 = ([1,2,3], 6)
test2 = ([-1,-2,-3], -6)
test3 = ([3,0,-3], 0)

test_dict = {
    "test1":test1,
    "test2":test2,
    "test3":test3
}

def answer1(ls):
    return(sum(ls))

def answer2(ls):
    return(sum(ls) - 1)

def answer3(ls):
    return(sum(ls) - 2)

answer_dict = {
    "answer1":answer1,
    "answer2":answer2,
    "answer3":answer3,
}



for (answer_name, answer) in answer_dict.items():
    for test_name, (test,sol) in test_dict.items():
        if (answer(test) == sol):
            print("[Example] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Example] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))


def time_tests(problem_number, answer_dict, test_dict, loops=1):
    for ((answer_name, answer),(test_name, (test,sol))) in zip(answer_dict.items(), test_dict.items()):
        time = timeit.timeit("{0}({1})".format(answer_name, test), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Example {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_tests(problem_number=1, answer_dict=answer_dict, test_dict=test_dict, loops=10000)

# [Example] Test: PASS, Function: answer1 Input: [1, 2, 3]
# [Example] Test: PASS, Function: answer1 Input: [-1, -2, -3]
# [Example] Test: PASS, Function: answer1 Input: [3, 0, -3]
# [Example] Test: FAIL, Function: answer2 Input: [1, 2, 3]
# [Example] Test: FAIL, Function: answer2 Input: [-1, -2, -3]
# [Example] Test: FAIL, Function: answer2 Input: [3, 0, -3]
# [Example] Test: FAIL, Function: answer3 Input: [1, 2, 3]
# [Example] Test: FAIL, Function: answer3 Input: [-1, -2, -3]
# [Example] Test: FAIL, Function: answer3 Input: [3, 0, -3]
# [Example 1] Time: 0.00246 seconds on 10000 loops, Function: answer1
# [Example 1] Time: 0.00291 seconds on 10000 loops, Function: answer2
# [Example 1] Time: 0.00237 seconds on 10000 loops, Function: answer3



####### broken scenario #######

test_dict = {
    "test1":([1,2,3], 6),
    "test2":([1,2,3], 6),
    "test3":([1,2,3], 6)
}

def answer1(ls):
    return(sum(ls))

def answer2(ls):
    return(sum(ls) - 1)

def answer3(ls):
    return(sum(ls) - 2)

answer_dict = {
    "answer1":answer1,
    "answer2":answer2,
    "answer3":answer3,
}



for (answer_name, answer) in answer_dict.items():
    for test_name, (test,sol) in test_dict.items():
        if (answer(test) == sol):
            print("[Example] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Example] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))


def time_tests(problem_number, answer_dict, test_dict, loops=1):
    for ((answer_name, answer),(test_name, (test,sol))) in zip(answer_dict.items(), test_dict.items()):
        time = timeit.timeit("{0}({1})".format(answer_name, test), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Example {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_tests(problem_number=1, answer_dict=answer_dict, test_dict=test_dict, loops=10000)

