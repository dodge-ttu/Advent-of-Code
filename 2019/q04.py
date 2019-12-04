from aocd.models import Puzzle
import numpy as np
from itertools import groupby

puzzle = Puzzle(year=2019, day=4)

data = puzzle.input_data
low_end, high_end = int(data.split('-')[0]), int(data.split('-')[1])

def criteria_check_any_repeats(low, high):
    all_options = np.arange(low, high+1)
    qualified_options = []
    for option in all_options:
        each_number = [int(s) for s in list(str(option))]
        checked_number = []
        for (idx, i) in enumerate(each_number):
            # First
            if idx == 0:
                if ((each_number[idx + 1] - i) >= 0):
                    checked_number.append(i)
            else:
                if ((i - each_number[idx - 1]) >= 0):
                    checked_number.append(i)
        if len(checked_number) == 6:
            groups_nums = [list(v) for (k, v) in groupby(checked_number)]
            group_lengths = [len(l) for l in groups_nums]
            group_lengths = [i for i in group_lengths if i > 1]
            if len(group_lengths) >= 1:
                qualified_number = int(''.join([str(i) for i in checked_number]))
                qualified_options.append(qualified_number)
    return qualified_options

qual_opts_any_repeats = criteria_check_any_repeats(low=low_end, high=high_end)
a_answer = len(qual_opts_any_repeats)

def criteria_check_no_bigger_groups(low, high):
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
        if (len(checked_number) == 6) :
            groups_nums = [list(v) for (k, v) in groupby(checked_number)]
            group_lengths = [len(l) for l in groups_nums]
            qualified_number = int(''.join([str(i) for i in checked_number]))
            if 2 in set(group_lengths):
                qualified_options.append(qualified_number)
    return qualified_options

qual_opts_no_bigger = criteria_check_no_bigger_groups(low=low_end, high=high_end)
b_answer = len(qual_opts_no_bigger)

# Puzzle metadata
def time_to_HHMMSS(td):
    HH = f'{(td // 3600):02d}'
    MM = f'{((td % 3600) // 60):02d}'
    SS = f'{((td % 3600) % 60):02d}'
    return HH, MM, SS

a_stats = puzzle.my_stats['a']
b_stats = puzzle.my_stats['b']

HHA, MMA, SSA = time_to_HHMMSS(a_stats['time'].seconds)
HHB, MMB, SSB = time_to_HHMMSS(b_stats['time'].seconds)
rank_a, score_a = a_stats['rank'], a_stats['score']
rank_b, score_b = b_stats['rank'], a_stats['score']

print(f'[INFO] Puzzle - {puzzle.title}')
print(f'[INFO] Part A - current answer: {a_answer} verified solution: {puzzle.answer_a}')
print(f'[INFO] Part A - time to solve: {HHA} hours {MMA} minutes {SSA} seconds')
print(f'[INFO] Part A - rank: {rank_a} score: {score_a}')
print(f'[INFO] Part B - current answer: {b_answer} verified solution: {puzzle.answer_b}')
print(f'[INFO] Part B - time to solve: {HHB} hours {MMB} minutes {SSB} seconds')
print(f'[INFO] Part B - rank: {rank_b} score: {score_b}')
