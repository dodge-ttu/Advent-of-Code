import math
from aocd.models import Puzzle
import numpy as np
import matplotlib.pyplot as plt

puzzle = Puzzle(year=2019, day=10)
data = puzzle.input_data

test_1 = '.#..#\n.....\n#####\n....#\n...##'
test_2 = '......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####'
test_3 = '#.#...#.#.\n.###....#.\n.#....#...\n##.#.#.#.#\n....#.#.#.\n.##..###.#\n..#...##..\n..##....##\n......#...\n.####.###.'
test_4 ='.#..#..###\n####.###.#\n....###.#.\n..###.##.#\n##.##.#.#.\n....###..#\n..#.#..#.#\n#..#.#.###\n.##...##.#\n.....#.#..'
test_5 = '.#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n.#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n#.#.#.#####.####.###\n###.##.####.##.#..##'

test = data.split('\n')
cleaned = []
for row in test:
    cleaned_row = []
    for item in row:
        item = 1 if item == '#' else 0
        cleaned_row.append(item)
    cleaned.append(cleaned_row)

map = np.array(cleaned)
h,w = map.shape

yy, xx = np.where(map == 1)

def count_visible_asteroids(xx,yy,h,w):
    asteroid_locs_and_count = []

    for (x1,y1) in zip(xx, yy):
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
        # ax.invert_yaxis()
        # ax.plot(xx, yy, color='blue', marker='o', linestyle='', markersize=1)
        # ax.set_axis_off()
        this_asteroids_vis_count = 0
        for (x2,y2) in zip(xx, yy):
            if (x1,y1) != (x2,y2):
                # y = m*x + b
                # Determine the equation of the line between the two asteroids
                delta_y = y2-y1
                delta_x = x2-x1
                # Check to see if any other asteroids are on that line, if so (x2,y2) is blocked.
                count = 0
                for (xcheck, ycheck) in zip(xx,yy):
                    s1 = ''
                    s2 = ''
                    if (min(x1, x2) <= xcheck <= max(x1, x2)) and (min(y1, y2) <= ycheck <= max(y1, y2)):
                        if ((xcheck,ycheck) != (x1,y1)) and ((xcheck,ycheck) != (x2,y2)):
                            if (delta_x == 0):
                                if x1 == xcheck:
                                    s1 = f'equation for line {x1, y1}---{x2, y2}: x={x1}'
                                    s2 = f'asteroid at {xcheck, ycheck} on this line'
                                    count += 1
                            elif (delta_y == 0):
                                if y1 == ycheck:
                                    s1 = f'equation for line {x1, y1}---{x2, y2}: x={y1}'
                                    s2 = f'asteroid at {xcheck, ycheck} on this line'
                                    count += 1
                            else:
                                m = (y2 - y1) / (x2 - x1)
                                b = y1 - m * x1
                                if math.isclose(ycheck, (m*xcheck + b), abs_tol=1e-5):
                                    print(ycheck, (m*xcheck+b))
                                    s1 = f'equation for line {x1, y1}---{x2, y2}: y = {m}*x + {b}'
                                    s2 = f'asteroid at {xcheck, ycheck} on this line'
                                    count += 1
                            #if s1:
                                #print(s1)
                                #print(s2)
                if count == 0:
                    this_asteroids_vis_count += 1
                    ax.plot([x1,x2], [y1,y2], color='red', linestyle='dotted', linewidth=0.8)
                    ax.plot(x2,y2, color='green', marker='o', linestyle='', markersize=2)
        asteroid_locs_and_count.append(((x1,y1), this_asteroids_vis_count, fig))

    return max(asteroid_locs_and_count, key=lambda x: x[1])

answer_cords, a_answer, plot_of_map = count_visible_asteroids(xx,yy,h,w)
print(a_answer)

def giant_laser_time(map, xx, yy, detectable_coords, location):
    asteroid_locs_and_count = []

        this_asteroids_vis_count = 0
        for (x2, y2) in zip(xx, yy):
            if (x1, y1) != (x2, y2):
                # y = m*x + b
                # Determine the equation of the line between the two asteroids
                delta_y = y2 - y1
                delta_x = x2 - x1
                # Check to see if any other asteroids are on that line, if so (x2,y2) is blocked.
                count = 0
                for (xcheck, ycheck) in zip(xx, yy):
                    s1 = ''
                    s2 = ''
                    if (min(x1, x2) <= xcheck <= max(x1, x2)) and (min(y1, y2) <= ycheck <= max(y1, y2)):
                        if ((xcheck, ycheck) != (x1, y1)) and ((xcheck, ycheck) != (x2, y2)):
                            if (delta_x == 0):
                                if x1 == xcheck:
                                    s1 = f'equation for line {x1, y1}---{x2, y2}: x={x1}'
                                    s2 = f'asteroid at {xcheck, ycheck} on this line'
                                    count += 1
                            elif (delta_y == 0):
                                if y1 == ycheck:
                                    s1 = f'equation for line {x1, y1}---{x2, y2}: x={y1}'
                                    s2 = f'asteroid at {xcheck, ycheck} on this line'
                                    count += 1
                            else:
                                m = (y2 - y1) / (x2 - x1)
                                b = y1 - m * x1
                                if math.isclose(ycheck, (m * xcheck + b), abs_tol=1e-5):
                                    print(ycheck, (m * xcheck + b))
                                    s1 = f'equation for line {x1, y1}---{x2, y2}: y = {m}*x + {b}'
                                    s2 = f'asteroid at {xcheck, ycheck} on this line'
                                    count += 1
                            # if s1:
                            # print(s1)
                            # print(s2)
                if count == 0:
                    this_asteroids_vis_count += 1
                    ax.plot([x1, x2], [y1, y2], color='red', linestyle='dotted', linewidth=0.8)
                    ax.plot(x2, y2, color='green', marker='o', linestyle='', markersize=2)
        asteroid_locs_and_count.append(((x1, y1), this_asteroids_vis_count, fig))

    return max(asteroid_locs_and_count, key=lambda x: x[1])



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
