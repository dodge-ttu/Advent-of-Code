import numpy as np
from itertools import groupby
from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=4)

data = puzzle.input_data
low_end, high_end = int(data.split('-')[0]), int(data.split('-')[1])

def criteria_check(low, high):
    all_options = np.arange(low, high+1)
    qualified_options = []
    for option in all_options:
        check_double = False
        replicated_digits = []
        each_number = [int(s) for s in list(str(option))]
        old_num = each_number[0]
        checked_number = []
        for i in each_number:
            if ((i-old_num) >= 0):
                checked_number.append(i)
                if (old_num == i):
                    check_double = True
                    replicated_digits.append(i)
                old_num = i
        if (len(checked_number) == 6) and (len(replicated_digits) > 1):
            qualified_options.append(int(''.join([str(i) for i in checked_number])))
        elif (len(checked_number) == 6) and (len(replicated_digits) == 1):
            print(int(''.join([str(i) for i in checked_number])))
    return qualified_options

qual_opts = criteria_check(low=low_end, high=high_end)
print(len(qual_opts))


def criteria_check(low, high):
    all_options = np.arange(low,high+1)
    qualified_options = []
    for option in all_options:
        each_number = [int(s) for s in list(str(option))]
        checked_number = []
        for (idx,i) in enumerate(each_number):
            # First
            if idx == 0:
                if ((each_number[idx+1]-i) >= 0):
                    checked_number.append(i)
            else:
                if ((i - each_number[idx-1]) >= 0):
                    checked_number.append(i)
        groups_nums = [list(v) for (k,v) in groupby(checked_number)]
        if (len(checked_number) == 6) :
            group_lengths = [len(l) for l in groups_nums]
            qualified_number = int(''.join([str(i) for i in checked_number]))
            if 2 in set(group_lengths):
                qualified_options.append(qualified_number)
    return qualified_options

qual_opts = criteria_check(low=low_end, high=high_end)
print(len(qual_opts))

