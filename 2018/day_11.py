from aocd import get_data
import numpy as np
import timeit


#data = get_data(day=11, year=2018)
# Data for this day as a single input that becomes the grid serial number.
# grid_serial_number = int(data)

# >>> print(grid_serial_number)
# 5235

grid_serial_number = 5235

##### PROBLEM 1 #####

### Test cases:
p1_a = (18, (33,45,29,18))
p1_b = (42, (21,61,30,42))

p1_test_cases = {
    "p1_a":p1_a,
    "p1_b":p1_b,
}

### Answers:
def power_by_location(x, y, serial):

    rack_id = x + 10
    power_level = rack_id * y
    power_level = power_level + serial
    power_level = power_level * rack_id
    power_level = int(str(round(power_level))[-3]) if power_level > 100 else 0
    power_level = power_level - 5

    return power_level

# test1 = -5 == power_by_location(122, 79, 57)
# test2 = 0 == power_by_location(217, 196, 39)
# test3 = 4 == power_by_location(101, 153, 71)
#
# print(f'[INFO] Test 1 Pass: {test1}')
# print(f'[INFO] Test 2 Pass: {test2}')
# print(f'[INFO] Test 3 Pass: {test3}')

def p1answer1(grid_serial_number, print_info=None):

    cell_power_info = []

    for x in range(1,298,1):
        for y in range(1,298,1):

            power_values = []

            for x_cell in range(x,x+3,1) :
                for y_cell in range(y,y+3,1):
                    pv = power_by_location(x_cell,y_cell,grid_serial_number)
                    power_values.append(pv)

            cell_power = sum(power_values)

            if len(power_values) < 9:
                print(x,y,cell_power)

            cell_power_info.append((x,y,cell_power))

    max_x, max_y, max_power = max(cell_power_info, key=lambda x: x[2])

    if print_info:
        print(f'X: {max_x}, Y: {max_y}, Power: {max_power}, Grid Serial Number: {grid_serial_number}')

    return  max_x, max_y, max_power, grid_serial_number


def p1answer2(grid_serial_number, print_info=None):

    cell_grid = np.ones((300,300))
    my_xx, my_yy = np.nonzero(cell_grid)

    gpv = np.vectorize(power_by_location)
    a = gpv(my_xx, my_yy, grid_serial_number).reshape(300,300)

    def power_per_cell(x, y, serial):

        if (x < 297) & (y < 297):
            this_cell_power = a[x:x+3, y:y+3].sum()

        else:
            this_cell_power = -5

        return (x, y, this_cell_power)

    ppv = np.vectorize(power_per_cell)
    b = ppv(my_xx, my_yy, grid_serial_number)
    b = [(a,b,c) for (a,b,c) in zip(b[0],b[1],b[2])]

    max_x, max_y, max_power = (max(b, key=lambda x: x[2]))

    if print_info:
        print(f'X: {max_x}, Y: {max_y}, Power: {max_power}, Grid Serial Number: {grid_serial_number}')

    return max_x, max_y, max_power, grid_serial_number

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


##### PROBLEM 2 #####

### Test Cases:
p2_a = (18, (90,269,16,18))
p2_b = (42, (232,251,12,42))

p2_test_cases = {
    "p2_a":p2_a,
    "p2_b":p2_b,
}

### Answers:
def p2answer1(grid_serial_number, print_info=None):

    cell_grid = np.ones((300, 300))
    my_xx, my_yy = np.nonzero(cell_grid)

    gpv = np.vectorize(power_by_location)
    cell_grid = gpv(my_xx, my_yy, grid_serial_number).reshape(300, 300)

    cell_power_info = []

    for (x,y) in zip(my_xx, my_yy):
        for b in range(300-x):
            cell_power = cell_grid[y:y+b, x:x+b].sum()
            cell_size = b

            cell_power_info.append((x,y, cell_size, cell_power))

    max_y, max_x, max_cell_size, max_power = max(cell_power_info, key=lambda x: x[3])

    if print_info:
        print(f'X: {max_x}, Y: {max_y}, Power: {max_power}, Size: {max_cell_size} x {max_cell_size}, Grid Serial Number: {grid_serial_number}')

    return max_x, max_y, max_cell_size, grid_serial_number


p2answers = {
    'p2answer1':p2answer1,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test, print_info=True) == sol):
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

data = grid_serial_number
time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Test: PASS, Function: p1answer1 Input: 18
# [Problem 1] Test: PASS, Function: p1answer1 Input: 42
# [Problem 1] Test: PASS, Function: p1answer2 Input: 18
# [Problem 1] Test: PASS, Function: p1answer2 Input: 42
# [Problem 2] Test: PASS, Function: p2answer1 Input: 18
# [Problem 2] Test: PASS, Function: p2answer1 Input: 42
# [Problem 1] Time: 0.48372 seconds on 1 loops, Function: p1answer1
# [Problem 1] Time: 0.26841 seconds on 1 loops, Function: p1answer2
# [Problem 2] Time: 126.85822 seconds on 1 loops, Function: p2answer1
