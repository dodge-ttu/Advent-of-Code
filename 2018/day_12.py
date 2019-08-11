from aocd import get_data
import timeit
import matplotlib.pyplot as plt

import numpy as np

data = get_data(day=12, year=2018)

##### PROBLEM 1 #####

### Test cases:
p1_a = ((
    [
    '...## => #',
    '..#.. => #',
    '.#... => #',
    '.#.#. => #',
    '.#.## => #',
    '.##.. => #',
    '.#### => #',
    '#.#.# => #',
    '#.### => #',
    '##.#. => #',
    '##.## => #',
    '###.. => #',
    '###.# => #',
    '####. => #',
    ],
    '#..#.#..##......###...###',),
    325)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:
def p1answer1(data, generations=20, test=False):
    if test:
        instructions = data[0]
        state = data[1]
    else:
        state_info = data.split('\n')
        state = state_info[0]
        state = state.split(' ')[2]
        instructions = state_info[2:]

    instructions = [s.split(' => ') for s in instructions]
    padding = generations + 10
    state = ''.join(['.']*padding) + state + ''.join(['.']*padding)
    state = list(state)
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
                if target == match_site:
                    state[i+2] = progeny

    plant_ids = []
    for (i,pot) in enumerate(state):
        if pot == '#':
            plant_ids.append(i-padding)

    id_sum = sum(plant_ids)
    state_sum_history.append(id_sum)
    gen_hist.append(gen)

    print(f'Solution for probelm 1: {id_sum}')

    return id_sum


p1answers = {
    "p1answer1":p1answer1,
}


### Problem 1 tests:
for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test, test=True) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))


##### PROBLEM 2 #####

# Problem two asks to carry problem one to 50 billion generations. My only hope find a solution was to fit a curve.
# when plotted I realized that the increase in the pot id sum becomes linear after a point. This is because a solid
# series of pots becomes full, then only the edges of that "chunk" expand and the pot id sum increases linearly.
# So I could easily fit a line and predict the pot id sum out to 50 billion.


### Test Cases:
p2_a = (0,0)
p2_b = (0,0)

p2_test_cases = {
    'p1_a':p2_a,
    'p1_b':p2_b,
}

### Answers:
def p2answer1(data, generations=800):
    state_info = data.split('\n')
    state = state_info[0]
    state = state.split(' ')[2]
    instructions = state_info[2:]
    instructions = [s.split(' => ') for s in instructions]
    padding = generations + 10
    state = ''.join(['.'] * padding) + state + ''.join(['.'] * padding)
    state = list(state)
    state_sum_history = []
    gen_hist = []

    for gen in range(1, generations + 1):
        if gen % 100 == 0:
            print(gen)
        gen_state = state.copy()
        state = ['.'] * len(state)
        for (target, progeny) in instructions:
            for i in range(len(state) - len(target) + 1):
                match_site = ''.join(gen_state[i:len(target) + i])
                if target == match_site:
                    state[i + 2] = progeny

        plant_ids = []
        for (i, pot) in enumerate(state):
            if pot == '#':
                plant_ids.append(i - padding)

        id_sum = sum(plant_ids)
        state_sum_history.append(id_sum)
        gen_hist.append(gen)

    fig, ax = plt.subplots(1,1, figsize=(20, 10))
    ax.plot(gen_hist, state_sum_history)
    ax.set_xlabel('Generation')
    ax.set_ylabel('Pot Id Sum')
    plt.title('Pot Id Sum Increase Over Time')
    plt.savefig('day_12_pot_sum_increase_over_time.png')

    x_linear = gen_hist[250:]
    y_linear = state_sum_history[250:]

    coeffs = np.polyfit(x_linear, y_linear, deg=1)
    poly_eqn = np.poly1d(coeffs)

    soln = poly_eqn(50_000_000_000)

    print(f'Solution for problem two: {int(soln)}')

    return int(soln)

p2answers = {
    'p2answer1':p2answer1,
}

### Problem 2 tests:

# for (answer_name, answer) in p2answers.items():
#     for test_name, (test,sol) in p2_test_cases.items():
#         if (answer(test) == sol):
#             print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
#         else:
#             print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))


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

# Solution for probelm 1: 325
# [Problem 1] Test: PASS, Function: p1answer1 Input: (['...## => #', '..#.. => #', '.#... => #', '.#.#. => #', '.#.## => #', '.##.. => #', '.#### => #', '#.#.# => #', '#.### => #', '##.#. => #', '##.## => #', '###.. => #', '###.# => #', '####. => #'], '#..#.#..##......###...###')
# [Problem 1] Time: 0.02568 seconds on 1 loops, Function: p1answer1
# [Problem 2] Time: 12.40946 seconds on 1 loops, Function: p2answer1
