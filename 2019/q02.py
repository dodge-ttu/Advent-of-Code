from aocd.models import Puzzle
import itertools

puzzle = Puzzle(year=2019, day=2)
data = puzzle.input_data

opcode = data.split(',')
opcode = [int(c) for c in opcode]

opcode[1] = 12
opcode[2] = 2

# Part A
def read_opcode(opcode):
    for i in range(0,len(opcode),4):
        one = opcode[opcode[i+1]]
        two = opcode[opcode[i+2]]
        if opcode[i] == 1:
            new_value = one + two
            opcode[opcode[i+3]] = new_value
        elif opcode[i] == 2:
            new_value = one * two
            opcode[opcode[i+3]] = new_value
        elif opcode[i] == 99:
            break

read_opcode(opcode)
a_answer = opcode[0]

# Part B
opcode = data.split(',')
opcode = [int(c) for c in opcode]

pairs = itertools.permutations(range(100), 2)

while True:
    a = opcode.copy()
    a[1], a[2] = next(pairs)
    read_opcode(a)
    if a[0] == 19690720:
        noun = a[1]
        verb = a[2]
        break

b_answer = 100 * noun + verb

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
