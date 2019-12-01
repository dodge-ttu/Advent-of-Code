from aocd.models import Puzzle
puzzle = Puzzle(year=2019, day=1)

masses = puzzle.input_data.split('\n')
masses = [int(i) for i in masses]

# Problem 1
def calc_fuel(x):
    x = int((x / 3)) - 2
    return x

required_fuel = []
for i in masses:
    required_fuel.append(calc_fuel(i))

p1_answer = sum(required_fuel)
print(f'[INFO] Problem one solution: {p1_answer}')

# Problem 2
def calc_fuels_fuel(x):
    fuels = []
    while x > 0:
        x = calc_fuel(x)
        if x < 0:
            x = 0
        fuels.append(x)

    return sum(fuels)

fuels_fuel = []
for i in masses:
    fuels_fuel.append(calc_fuels_fuel(i))

p2_answer = sum(fuels_fuel)
print(f'[INFO] Problem two solution: {p2_answer}')

