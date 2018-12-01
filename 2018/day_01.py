# Answer one was nothing more than a summation of a list of integers.
sum([1,-2,3])

# Terrible, hacky solution. Improvements pending.
import pandas as pd

df = pd.read_csv("/home/will/advent_of_code/Advent-of-Code/2018/day_01_input.txt", header=None)
values = list(df.loc[:, 0].values) * 100000

# This solution takes about 3 minutes 39 seconds.
def answer(ls):
    sums = []
    count = 0
    sum = 0
    while True:
        if (sum + ls[count]) in sums:
            print(sum + ls[count])
            break
        else:
            print(sum, ls[count])
            sum += (ls[count])
            count += 1
            sums.append(sum)

answer(values)

# Maybe generator solution without pandas.
import csv
import itertools

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_01_input.txt"

with open(file_path, newline='') as csv_file:
    raw_data = csv.reader(csv_file, delimiter=" ", quoting=csv.QUOTE_NONNUMERIC)
    data = []
    for i in list(raw_data):
        data.extend(i)

print(data)

# This solution takes about 1 minute 21 seconds.
def answer2(ls, sums = [], count = 0, sum = 0):
    for i in itertools.cycle(ls):
        if (sum + i) in sums:
            print(sum + i)
            break
        else:
            print(sum, i)
            sum += (i)
            count += 1
            sums.append(sum)

answer2(data)




