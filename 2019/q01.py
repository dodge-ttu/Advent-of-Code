from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=1)
data = puzzle.input_data

masses = data.split('\n')
masses = [int(i) for i in masses]

# Part A
def calc_fuel(x):
    x = int(x / 3) - 2
    if x < 0:
        x = 0
    return x

required_fuel = []
for i in masses:
    required_fuel.append(calc_fuel(i))

a_answer = sum(required_fuel)

# Part B
def calc_fuels_fuel(x):
    fuels = []
    while x > 0:
        x = calc_fuel(x)
        fuels.append(x)
    return sum(fuels)

fuels_fuel = []
for i in masses:
    fuels_fuel.append(calc_fuels_fuel(i))

b_answer = sum(fuels_fuel)

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
