from aocd.models import Puzzle
from itertools import combinations
import numpy as np
import re

puzzle = Puzzle(year=2019, day=12)
data = puzzle.input_data
init_pos = data.split('\n')

test = ['<x=-1, y=0, z=2>','<x=2, y=-10, z=-7>','<x=4, y=-8, z=8>','<x=3, y=5, z=-1>']
test2 = ['<x=-8, y=-10, z=0>','<x=5, y=5, z=10>','<x=2, y=-7, z=3>','<x=9, y=-8, z=-3>']

def create_universe(init_pos):
    p = re.compile(r'-?\d+')
    i, e, g, c = init_pos

    ii = [int(s) for s in p.findall(i)]
    ee = [int(s) for s in p.findall(e)]
    gg = [int(s) for s in p.findall(g)]
    cc = [int(s) for s in p.findall(c)]

    planets = ['Io', 'Europa', 'Ganymede', 'Callisto']
    plan_comb = [pt for pt in combinations(planets, 2)]

    io = {
        'pos': {'x': ii[0], 'y': ii[1], 'z': ii[2]},
        'vel': {'x': 0, 'y': 0, 'z': 0},
        'pot': 0,
        'kin': 0,
        'tot': 0,
    }
    eu = {
        'pos': {'x': ee[0], 'y': ee[1], 'z': ee[2]},
        'vel': {'x': 0, 'y': 0, 'z': 0},
        'pot': 0,
        'kin': 0,
        'tot': 0,
    }
    ga = {
        'pos': {'x': gg[0], 'y': gg[1], 'z': gg[2]},
        'vel': {'x': 0, 'y': 0, 'z': 0},
        'pot': 0,
        'kin': 0,
        'tot': 0,
    }
    ca = {
        'pos': {'x': cc[0], 'y': cc[1], 'z': cc[2]},
        'vel': {'x': 0, 'y': 0, 'z': 0},
        'pot': 0,
        'kin': 0,
        'tot': 0,
    }

    planets = {
        'Io': io,
        'Europa': eu,
        'Ganymede': ga,
        'Callisto': ca,
    }

    return planets, plan_comb

def pos_vel_update(planets, plan_comb):
    for (n1, n2) in plan_comb:
        x1, y1, z1 = planets[n1]['pos']['x'], planets[n1]['pos']['y'], planets[n1]['pos']['z']
        x2, y2, z2 = planets[n2]['pos']['x'], planets[n2]['pos']['y'], planets[n2]['pos']['z']
        if x1 > x2:
            planets[n1]['vel']['x'] -= 1
            planets[n2]['vel']['x'] += 1
        elif x1 < x2:
            planets[n1]['vel']['x'] += 1
            planets[n2]['vel']['x'] -= 1
        if y1 > y2:
            planets[n1]['vel']['y'] -= 1
            planets[n2]['vel']['y'] += 1
        elif y1 < y2:
            planets[n1]['vel']['y'] += 1
            planets[n2]['vel']['y'] -= 1
        if z1 > z2:
            planets[n1]['vel']['z'] -= 1
            planets[n2]['vel']['z'] += 1
        elif z1 < z2:
            planets[n1]['vel']['z'] += 1
            planets[n2]['vel']['z'] -= 1
    for planet_name in planets.keys():
        planets[planet_name]['pos']['x'] += planets[planet_name]['vel']['x']
        planets[planet_name]['pos']['y'] += planets[planet_name]['vel']['y']
        planets[planet_name]['pos']['z'] += planets[planet_name]['vel']['z']

    return planets

def check_complete_period(planets, plan_comb, ax):

    in_io_x = planets['Io']['pos'][ax]
    in_io_v = planets['Io']['vel'][ax]
    in_eu_x = planets['Europa']['pos'][ax]
    in_eu_v = planets['Europa']['vel'][ax]
    in_ga_x = planets['Ganymede']['pos'][ax]
    in_ga_v = planets['Ganymede']['vel'][ax]
    in_ca_x = planets['Callisto']['pos'][ax]
    in_ca_v = planets['Callisto']['vel'][ax]

    init_x = f'{in_io_x}:{in_io_v}:{in_eu_x}:{in_eu_v}:{in_ca_x}:{in_ca_v}:{in_ga_x}:{in_ga_v}'
    cur_x = ''
    count = 0

    while init_x != cur_x:

        planets = pos_vel_update(planets, plan_comb)

        in_io_x = planets['Io']['pos'][ax]
        in_io_v = planets['Io']['vel'][ax]
        in_eu_x = planets['Europa']['pos'][ax]
        in_eu_v = planets['Europa']['vel'][ax]
        in_ga_x = planets['Ganymede']['pos'][ax]
        in_ga_v = planets['Ganymede']['vel'][ax]
        in_ca_x = planets['Callisto']['pos'][ax]
        in_ca_v = planets['Callisto']['vel'][ax]

        count += 1

        cur_x = f'{in_io_x}:{in_io_v}:{in_eu_x}:{in_eu_v}:{in_ca_x}:{in_ca_v}:{in_ga_x}:{in_ga_v}'

    return count

# Part A
planets, plan_comb = create_universe(init_pos)

for i in range(1000):
    planets = pos_vel_update(planets, plan_comb)

for planet_name in planets.keys():
    planets[planet_name]['pot'] += abs(planets[planet_name]['pos']['x']) + \
                                   abs(planets[planet_name]['pos']['y']) + \
                                   abs(planets[planet_name]['pos']['z'])
    planets[planet_name]['kin'] += abs(planets[planet_name]['vel']['x']) + \
                                   abs(planets[planet_name]['vel']['y']) + \
                                   abs(planets[planet_name]['vel']['z'])
    planets[planet_name]['tot'] = planets[planet_name]['pot'] * planets[planet_name]['kin']

a_answer = sum([v['tot'] for (k,v) in planets.items()])

# Part B
periods =[]

for ax in ['x','y','z']:
    planets, plan_comb = create_universe(init_pos)
    period_length = check_complete_period(planets, plan_comb, ax)
    periods.append(period_length)

b_answer = np.lcm.reduce(periods)

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
