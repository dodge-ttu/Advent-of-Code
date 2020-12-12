from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=2)
data = puzzle.input_data.splitlines()

# Part A
def valid_pass(x):
    count = 0
    for i in x:
        info = i.split(' ')
        limits = info[0].split('-')
        minlim = int(limits[0])
        maxlim = int(limits[1])
        letter = info[1][0]
        password = info[2]
        letter_count = sum([1 for l in password if l == letter])
        if minlim <= letter_count <= maxlim:
            count+=1
    return count

a_answer = valid_pass(data)

# Part B
def valid_pass_again(x):
    count = 0
    for i in x:
        info = i.split(' ')
        limits = info[0].split('-')
        loc1 = int(limits[0])
        loc2 = int(limits[1])
        letter = info[1][0]
        password = info[2]
        check1 = (letter == password[loc1-1])
        check2 = (letter == password[loc2-1])
        if (check1 or check2) and not (check1 & check2):
            count += 1
    return count

b_answer = valid_pass_again(data)

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
