# Terrible hacky solution. Improvements pending

import pandas as pd

df = pd.read_csv("/home/will/advent_of_code/Advent-of-Code/2018/day_01_input.txt", header=None)

values = list(df.loc[:, 0].values) * 100000

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



