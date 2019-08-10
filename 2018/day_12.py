from aocd import get_data
import timeit
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import AutoMinorLocator

import numpy as np

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
    state_info = data.split('\n')
    state = state_info[0]
    state = state.split(' ')[2]
    generations = 500
    padding = generations + 10
    state = ''.join(['.']*padding) + state + ''.join(['.']*padding)
    state = list(state)
    instructions = state_info[2:]
    instructions = [s.split(' => ') for s in instructions]
    # state = '#..#.#..##......###...###'
    # state = '.....' + state + ''.join(['.']*20)
    # state = list(state)
    # instructions = [
    #     '...## => #',
    #     '..#.. => #',
    #     '.#... => #',
    #     '.#.#. => #',
    #     '.#.## => #',
    #     '.##.. => #',
    #     '.#### => #',
    #     '#.#.# => #',
    #     '#.### => #',
    #     '##.#. => #',
    #     '##.## => #',
    #     '###.. => #',
    #     '###.# => #',
    #     '####. => #',
    # ]
    # instructions = [s.split(' => ') for s in instructions]

    #state_history = [''.join(state)]
    state_sum_history = []
    gen_hist = []

    for gen in range(1,generations+1):
        if gen % 100 == 0:
            print(gen)
        gen_state = state.copy()
        state = ['.'] * len(state)
        for (target, progeny) in instructions:
            for i in range(len(state) - len(target)+1):
                match_site = ''.join(gen_state[i:len(target)+i])
                #print(f'>>>{target} : {match_site}')
                if target == match_site:
                    state[i+2] = progeny
                    #print(f'>>>{target} equal to {match_site}')

        plant_ids = []
        for (i,pot) in enumerate(state):
            if pot == '#':
                plant_ids.append(i-padding)

        id_sum = sum(plant_ids)
        state_sum_history.append(id_sum)
        gen_hist.append(gen)

    fig, ax = plt.subplots(1,1, figsize=(20, 10))
    ax.plot(gen_hist, state_sum_history)
    #ax.xaxis.set_minor_locator(MultipleLocator(1))
    #ax.yaxis.set_minor_locator(MultipleLocator(10))
    #ax.grid(which='both')
    plt.show()

    gen_id = 12 -1
    print(state_sum_history[gen_id])

    x_linear = gen_hist[250:]
    y_linear = state_sum_history[250:]

    coeffs = np.polyfit(x_linear, y_linear, deg=1)
    poly_eqn = np.poly1d(coeffs)


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
