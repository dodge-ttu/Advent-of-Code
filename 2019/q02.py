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
part_a_answer = opcode[0]

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

part_b_answer = 100 * noun + verb

print(part_a_answer)
print(part_b_answer)
print(f'[INFO] Puzzle Title: {puzzle.title}')
print(f'[INFO] Part A answer: {puzzle.answer_a}')
print(f'[INFO] Part B answer: {puzzle.answer_b}')
