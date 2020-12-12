from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=1)
data = puzzle.input_data.splitlines()
data = [int(i) for i in data]

# Part A
def fix_exp_report(x):
    for i in x:
        for j in x:
            if j + i == 2020:
                return j*i

a_answer = fix_exp_report(data)

# Part B
def fix_exp_report_again(x):
    for i in x:
        for j in x:
            for k in x:
                if i + j + k == 2020:
                    return i*j*k

b_answer = fix_exp_report_again(data)

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
