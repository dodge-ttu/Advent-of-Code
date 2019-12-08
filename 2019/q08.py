from aocd.models import Puzzle
import numpy as np
import cv2

puzzle = Puzzle(year=2019, day=8)
data = puzzle.input_data

img_data = np.array([int(c) for c in data])
layers = []
for i in range(0, 15000, 150):
    layer = img_data[i:i+150]
    layer = layer.reshape(6,25)
    layers.append(layer)

fewest_zeros = []
for l in layers:
    u, c = np.unique(l, return_counts=True)
    counts_dict = dict(zip(u, c))
    fewest_zeros.append((counts_dict[0], l, counts_dict))

few_z = min(fewest_zeros, key=lambda x: x[0])
few_z_d = few_z[2]
a_answer = few_z_d[1] * few_z_d[2]
print(a_answer)

loc_top_pix = np.zeros((6,25), dtype=int)
stacked = np.array(layers)
first_visible = np.argmax(stacked < 2, axis=0)

# Really wish this indexing was better. Could produce an array with the first occurance
# of a visible pixel as if I was standing over the stack and looking down into it, but
# was forced to manually use the extract the pixels given once known on z axis.
for x in range(0,25):
    for y in range(0,6):
        z = first_visible[y,x]
        pix = stacked[z,y,x]
        loc_top_pix[y,x] = pix

img = loc_top_pix
img[img == 1] = 255

img = img.astype(np.uint8)
cv2.imwrite('/home/will/advent_of_code/Advent-of-Code/2019/aoc.png', img)
b_answer = 'ZUKCJ'

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

