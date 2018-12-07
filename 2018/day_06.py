import timeit
import csv

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

def p1answer1(ls):

    # Store the quantity of points closest to each centroid so that I can increase the "viewing" window with a two
    # part loop to determine if the count increases. The centroids where the count increases can be marked as infinite.
    counts = {str(k):0 for k in ls}
    loop_counter = 0

    for i in range(2):
        loop_counter += 1

        # Find max right centroid to set boundary
        distances_from_origin = []
        for (x,y) in ls:
            dist = abs(0-abs(x)) + abs(0-abs(y))
            distances_from_origin.append((dist, (x,y)))

        if loop_counter == 1:
            (min_x,min_y) = (0,0)
            (max_from_origin, (max_x,max_y)) = max([i for i in distances_from_origin], key=lambda x: x[0])

        if loop_counter == 2:
            (min_x, min_y) = (-100, -100)
            (max_from_origin, (max_x, max_y)) = max([i for i in distances_from_origin], key=lambda x: x[0])
            (max_x, max_y) = (max_x+100, max_y+100)

        print(min_x,min_y,max_x,max_y)

        # Generate all ordered pairs within boundary.
        all_points_within = []
        for x in range(min_x,max_x+1):
            for y in range(min_y,max_y+1):
                all_points_within.append((x,y))

        print("length points within: {0}".format(len(all_points_within)))

        # Distance from all centroids for each point.
        dist_all_for_all = {}
        for (x,y) in all_points_within:
            dist_this_for_all = {}
            for (x_centroid,y_centroid) in ls:
                dist = abs(x_centroid - x) + abs(y_centroid - y)
                dist_this_for_all[str((x_centroid,y_centroid))] = dist
            dist_all_for_all[str((x,y))] = dist_this_for_all

        # Associate minimum distance with centroids.
        # Also drop points that share centroid values.
        closest_centroid_to_each = {}
        for (x,y) in all_points_within:
            d = dist_all_for_all[str((x,y))]
            centroid_closest_to_this = min(d.items(), key=lambda x: x[1])
            all_that_map_to_that_centroid = [k for k in d if d[k] == centroid_closest_to_this[1]]
            if len(all_that_map_to_that_centroid) == 1:
                closest_centroid_to_each[str((x,y))] = centroid_closest_to_this[0]

        # First pass...
        if loop_counter == 1:
            # Find centroid with max associated closest items, figures crossed...
            counts = []
            for (x_centroid,y_centroid) in ls:
                count = sum(value == str((x_centroid,y_centroid)) for value in closest_centroid_to_each.values())
                counts.append((str((x_centroid,y_centroid)), count))

            print("length counts first time: {0}".format(len(counts)))

            centroid_with_max_closest = max(counts, key=lambda x: x[1])

            print(centroid_with_max_closest)

        # Second pass...
        if loop_counter == 2:
            # Check to see which centroids have an increase in associated points to filter out the infinite centroids.
            # Find centroid with max associated closest items, figures crossed...
            counts_second_time = []
            for (x_centroid, y_centroid) in ls:
                count = sum(value == str((x_centroid, y_centroid)) for value in closest_centroid_to_each.values())
                counts_second_time.append((str((x_centroid, y_centroid)), count)

            marked_centroids = []

            for (c1,c2) in zip(counts, counts_second_time):
                if c1 < c2:
                    marked_centroids.append(c1)

            for key in marked_centroids:
                    counts.remove(key)

            print("length counts second time: {0}".format(len(counts_second_time)))

            centroid_with_max_closest = max(counts, key=lambda x: x[1])

            print(centroid_with_max_closest)

            return centroid_with_max_closest[1], counts_second_time

def p1answer2(*args, **kwargs):
    pass

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

with open(file_path) as my_file:
    raw_data = csv.reader(my_file, quoting=csv.QUOTE_NONNUMERIC)
    data = []
    for row in raw_data:
        data.append((int(row[0]),int(row[1])))

# Data was the same for problem one and two for this day.



####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data, testing=False)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1, testing=False)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# NOTE: This one seems to be a bit more challenging. Having never encountered a problem such as this I think
# outlining a process beforehand may help rather than trudging through with nothing more than a half-baked
# mental model :) ... nevermind, it's all half baked.
#
# Step one:     Find upper left and lower right to define "viewing" space.
# Step two:     Mark any case on boundary lines (or one away from boundary) as guaranteed to be infinite.
# Step three:   Find distance from a given centroid and all points in "viewing" space. (Yikes that's alot)
# Step four:    For each point in the "viewing" space find unmarked centroid with minimal associated distance.
# Step five:    Centroid associated with most points wins..... or
# Step seven:   Cry like a baby and try to erase advent of code from memory (:
#
# DO NOT USE PARENTHESIS ON RETURN STATEMENTS !!! Can't believe I have been doing that.
#
# Do not use "dict" as variable name because it shadows built-in type!
#
# https://stackoverflow.com/a/3282871/7384740
# Cleaner way to run min/max on dictionary:
# max(d.items(), key=lambda x: x[1]) will look at the value.
# max(d.items(), key-lambda x: x[0]) will look at the key.
#
# https://stackoverflow.com/a/48371928/7384740
# Count occurrences of a value in dictionary:
# sum(value == 0 for value in d.values())
#
# Step two: This original method of filtering will miss many cases. The only thing I can think to do at this point is
# to increase the viewing space with a short loop and only look at counts that increase to separate finite from
# infinite.
#
#
#
#
#
#


