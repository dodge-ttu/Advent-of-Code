# NOTES: This one seems to be a bit more challenging. Having never encountered a problem such as this I think
# outlining a process beforehand may help rather than trudging through with nothing more than a half-baked
# mental model :)
#
# Step one:     Find pair furthest from origin to define "viewing" space.
# Step two:     Drop any case one away from boundary as guaranteed to be infinite.
# Step three:   Find distance from a given pair and all points in "viewing" space. (Yikes that's alot)
# Step four:    For each point in the "viewing" space find centroid with minimal associated distance.
# Step five:    Pop value from all dicts except that with the minimally associated distance.
# Step six:     Finite distances can be defined as those with a pair in all other dicts, right?!?.....
# Step seven:   Cry like a baby and try to erase advent of code from memory :)

import timeit
import math
import operator
import re

####### Problem 1 #######

# Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y
# locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

# Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list
# of coordinates:

# 1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9

# If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

# ..........
# .A........
# ..........
# ........C.
# ...D......
# .....E....
# .B........
# ..........
# ..........
# ........F.

# This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each
# location's closest coordinate can be determined, shown here in lowercase:

# aaaaa.cccc
# aAaaa.cccc
# aaaddecccc
# aadddeccCc
# ..dDdeeccc
# bb.deEeecc
# bBb.eeee..
# bbb.eeefff
# bbb.eeffff
# bbb.ffffFf

# Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

# In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend
# forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations,
# and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of
# the largest area is 17.

# What is the size of the largest area that isn't infinite?

### Test cases:

p1_a = ([(1,1),(1,6),(8,3),(3,4),(5,5),(8,9)], 17)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

ls = p1_a[0]

def p1answer1(ls):

    # Find max centriod to set boundary
    distances_from_origin = []
    for (x,y) in ls:
        dist = abs(0-x) + abs(0-y)
        distances_from_origin.append(dist)

    # Determine if centriod is "one" away from edge and drop.

    print(distances_from_origin)

def p1answer2():

p1answers = {
    "p1answer1":p1answer1,
    "p1answer2":p1answer2,
}

### Problem 1 tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))




####### Problem 2 #######


### Test cases:

p2_a =

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1():




def p2answer2():

p2answers = {
    "p2answer1":p2answer1,
    "p2answer2":p2answer2,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))




####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_06_input.txt"

with open(file_path, "r") as my_file:
    data = my_file.read()

# Data was the same for problem one and two for this day.



####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data, testing=False)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1, testing=False)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)


# NOTES: This one seems to be a bit more challenging. Having never encountered a problem such as this I think
# outlining a process beforehand may help rather than trudging through with nothing more than a half-baked
# mental model :)
#
# Step one:     Find pair furthest from origin to define "viewing" space.
# Step two:     Drop any case one away from boundary as guaranteed to be infinite.
# Step three:   Find distance from a given pair and all points in "viewing" space. (Yikes that's alot)
# Step four:    For each point in the "viewing" space find centroid with minimal associated distance.
# Step five:    Pop value from all dicts except that with the minimally associated distance.
# Step six:     Finite distances can be defined as those with a pair in all other dicts, right?!?.....
# Step seven:   Cry like a baby and try to erase advent of code from memory :)
