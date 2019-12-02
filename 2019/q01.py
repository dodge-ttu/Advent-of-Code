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

part_a_answer = sum(required_fuel)
print(part_a_answer)

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

part_b_answer = sum(fuels_fuel)
print(part_b_answer)

print(f'[INFO] Puzzle Title: {puzzle.title}')
print(f'[INFO] Part A answer: {puzzle.answer_a}')
print(f'[INFO] Part B answer: {puzzle.answer_b}')
