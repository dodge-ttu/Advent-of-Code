from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2020, day=3)
data = puzzle.input_data.splitlines()
data = [list(row) for row in data]
data = np.array(data)

# Part A
def find_trees(map):
    count = 0
    x = 0
    y = 0
    h,w = map.shape
    while True:
        x+=3
        y+=1
        try:
            if x >= w:
                x = x%(w-1)-1
            if map[(y,x)] == '#':
                count+=1
        except:
            #print('You have reached the bottom')
            return count

a_answer = find_trees(data)

# Part B
def find_trees_variable_slope(map, slope):
    count = 0
    x=0
    y=0
    xinc,yinc = slope
    h,w = map.shape
    while True:
        x+=xinc
        y+=yinc
        try:
            if x >= w:
                x = x%(w-1)-1
            if map[(y,x)] == '#':
                count+=1
        except:
            #print('You have reached the bottom')
            return count

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
tree_counts = []
for slope in slopes:
    tree_count = find_trees_variable_slope(data, slope)
    tree_counts.append(tree_count)
b_answer = np.prod(np.array(tree_counts))

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
