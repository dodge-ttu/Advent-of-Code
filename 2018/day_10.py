import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#region Problem 1
#
# It's no use; your navigation system simply isn't capable of providing walking directions in the arctic circle,
# and certainly not in 1018.
#
# The Elves suggest an alternative. In times like these, North Pole rescue operations will arrange points of
# light in the sky to guide missing Elves back to base. Unfortunately, the message is easy to miss: the points
# move slowly enough that it takes hours to align them, but have so much momentum that they only stay aligned
# for a second. If you blink at the wrong time, it might be hours before another message appears.
#
# You can see these points of light floating in the distance, and record their position in the sky and their
# velocity, the relative change in position per second (your puzzle input). The coordinates are all given from
# your perspective; given enough time, those positions and velocities will move the points into a cohesive message!
#
# Rather than wait, you decide to fast-forward the process and calculate what the points will eventually spell.
#
# For example, suppose you note the following points:
#
# position=< 9,  1> velocity=< 0,  2>
# position=< 7,  0> velocity=<-1,  0>
# position=< 3, -2> velocity=<-1,  1>
# position=< 6, 10> velocity=<-2, -1>
# position=< 2, -4> velocity=< 2,  2>
# position=<-6, 10> velocity=< 2, -2>
# position=< 1,  8> velocity=< 1, -1>
# position=< 1,  7> velocity=< 1,  0>
# position=<-3, 11> velocity=< 1, -2>
# position=< 7,  6> velocity=<-1, -1>
# position=<-2,  3> velocity=< 1,  0>
# position=<-4,  3> velocity=< 2,  0>
# position=<10, -3> velocity=<-1,  1>
# position=< 5, 11> velocity=< 1, -2>
# position=< 4,  7> velocity=< 0, -1>
# position=< 8, -2> velocity=< 0,  1>
# position=<15,  0> velocity=<-2,  0>
# position=< 1,  6> velocity=< 1,  0>
# position=< 8,  9> velocity=< 0, -1>
# position=< 3,  3> velocity=<-1,  1>
# position=< 0,  5> velocity=< 0, -1>
# position=<-2,  2> velocity=< 2,  0>
# position=< 5, -2> velocity=< 1,  2>
# position=< 1,  4> velocity=< 2,  1>
# position=<-2,  7> velocity=< 2, -2>
# position=< 3,  6> velocity=<-1, -1>
# position=< 5,  0> velocity=< 1,  0>
# position=<-6,  0> velocity=< 2,  0>
# position=< 5,  9> velocity=< 1, -2>
# position=<14,  7> velocity=<-2,  0>
# position=<-3,  6> velocity=< 2, -1>
#
# Each line represents one point. Positions are given as <X, Y> pairs: X represents how far left (negative)
# or right (positive) the point appears, while Y represents how far up (negative) or down (positive) the
# point appears.
#
# At 0 seconds, each point has the position given. Each second, each point's velocity is added to its position.
# So, a point with velocity <1, -2> is moving to the right, but is moving upward twice as quickly. If this
# point's initial position were <3, 9>, after 3 seconds, its position would become <6, 3>.
#
# Over time, the points listed above would move like this:
#
# Initially:
# ........#.............
# ................#.....
# .........#.#..#.......
# ......................
# #..........#.#.......#
# ...............#......
# ....#.................
# ..#.#....#............
# .......#..............
# ......#...............
# ...#...#.#...#........
# ....#..#..#.........#.
# .......#..............
# ...........#..#.......
# #...........#.........
# ...#.......#..........
#
# After 1 second:
# ......................
# ......................
# ..........#....#......
# ........#.....#.......
# ..#.........#......#..
# ......................
# ......#...............
# ....##.........#......
# ......#.#.............
# .....##.##..#.........
# ........#.#...........
# ........#...#.....#...
# ..#...........#.......
# ....#.....#.#.........
# ......................
# ......................
#
# After 2 seconds:
# ......................
# ......................
# ......................
# ..............#.......
# ....#..#...####..#....
# ......................
# ........#....#........
# ......#.#.............
# .......#...#..........
# .......#..#..#.#......
# ....#....#.#..........
# .....#...#...##.#.....
# ........#.............
# ......................
# ......................
# ......................
#
# After 3 seconds:
# ......................
# ......................
# ......................
# ......................
# ......#...#..###......
# ......#...#...#.......
# ......#...#...#.......
# ......#####...#.......
# ......#...#...#.......
# ......#...#...#.......
# ......#...#...#.......
# ......#...#..###......
# ......................
# ......................
# ......................
# ......................
#
# After 4 seconds:
# ......................
# ......................
# ......................
# ............#.........
# ........##...#.#......
# ......#.....#..#......
# .....#..##.##.#.......
# .......##.#....#......
# ...........#....#.....
# ..............#.......
# ....#......#...#......
# .....#.....##.........
# ...............#......
# ...............#......
# ......................
# ......................
#
# After 3 seconds, the message appeared briefly: HI. Of course, your message will be much longer and will take
# many more seconds to appear.
#
# What message will eventually appear in the sky?
#
#endregion

### Test cases:

p1_a = ([
    "position=< 9,  1> velocity=< 0,  2>",
    "position=< 7,  0> velocity=<-1,  0>",
    "position=< 3, -2> velocity=<-1,  1>",
    "position=< 6, 10> velocity=<-2, -1>",
    "position=< 2, -4> velocity=< 2,  2>",
    "position=<-6, 10> velocity=< 2, -2>",
    "position=< 1,  8> velocity=< 1, -1>",
    "position=< 1,  7> velocity=< 1,  0>",
    "position=<-3, 11> velocity=< 1, -2>",
    "position=< 7,  6> velocity=<-1, -1>",
    "position=<-2,  3> velocity=< 1,  0>",
    "position=<-4,  3> velocity=< 2,  0>",
    "position=<10, -3> velocity=<-1,  1>",
    "position=< 5, 11> velocity=< 1, -2>",
    "position=< 4,  7> velocity=< 0, -1>",
    "position=< 8, -2> velocity=< 0,  1>",
    "position=<15,  0> velocity=<-2,  0>",
    "position=< 1,  6> velocity=< 1,  0>",
    "position=< 8,  9> velocity=< 0, -1>",
    "position=< 3,  3> velocity=<-1,  1>",
    "position=< 0,  5> velocity=< 0, -1>",
    "position=<-2,  2> velocity=< 2,  0>",
    "position=< 5, -2> velocity=< 1,  2>",
    "position=< 1,  4> velocity=< 2,  1>",
    "position=<-2,  7> velocity=< 2, -2>",
    "position=< 3,  6> velocity=<-1, -1>",
    "position=< 5,  0> velocity=< 1,  0>",
    "position=<-6,  0> velocity=< 2,  0>",
    "position=< 5,  9> velocity=< 1, -2>",
    "position=<14,  7> velocity=<-2,  0>",
    "position=<-3,  6> velocity=< 2, -1>",
        ], 0)

### Data:

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_10_input.txt"

with open(file_path) as my_file:
    raw_data = my_file.read().splitlines()
    data = []
    for row in raw_data:
        data.append(row)


### Answers:

def p1answer1(data):
    # Parse data.
    image_data = []

    for line in data:
        coords = re.findall(r"[+-]?(?<!\.)\b[0-9]+\b(?!\.[0-9])", line)
        coords = [int(i) for i in coords]

        image_data.append(coords)

    # Initial x values.
    xs = []
    for i in image_data:
        xs.append(i[0])

    # Initial y values.
    ys = []
    for i in image_data:
        ys.append(i[1])

    # X velocity increment.
    x_vols = []
    for i in image_data:
        x_vols.append(i[2])

    # Y velocity increment.
    y_vols = []
    for i in image_data:
        y_vols.append(i[3])

    # np array for convenience
    xs = np.array(xs)
    ys = np.array(ys)
    x_vols = np.array(x_vols)
    y_vols = np.array(y_vols)

    # Fast forward
    for i in range(10633):
        xs += x_vols
        ys += y_vols

    # Set up plotting area.
    fig, ax = plt.subplots()
    line, = ax.plot([], [], "o")

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    ax.set_xlim((min_x - 1000, max_x + 1000))
    ax.set_ylim((min_y - 1000, max_y + 1000))

    # Animation initilization function
    def init():
        line.set_data([], [])

        return line,

    #  Animation function.
    def animate(i, xs, ys, x_vols, y_vols):

        xs += x_vols
        ys += y_vols

        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)

        ax.set_xlim((min_x - (.1 * min_x)), (max_x + (.1 * max_x)))
        ax.set_ylim((min_y - (.1 * max_y)), (max_y + (.1 * max_y)))

        line.set_data(xs, ys)

        return line,

    fargs = (xs, ys, x_vols, y_vols)

    # Generate animation.
    anim = animation.FuncAnimation(fig, animate, blit=False, interval=300,
                                   repeat=True, init_func=init, fargs=fargs)
    plt.show()

    # Save a copy
    anim.save('/home/will/Desktop/animation.gif', writer='imagemagick', fps=1)


p1answers = {
    "p1answer1":p1answer1,
}

### Problem 1 tests:

# No testing, only visual inspection.


#region Problem 2
#
# How many seconds until the image appears?
#
#endregion

# Parse data.
image_data = []

for line in data:
    coords = re.findall(r"[+-]?(?<!\.)\b[0-9]+\b(?!\.[0-9])", line)
    coords = [int(i) for i in coords]

    image_data.append(coords)

# Initial x values.
xs = []
for i in image_data:
    xs.append(i[0])

# Initial y values.
ys = []
for i in image_data:
    ys.append(i[1])

# X velocity increment.
x_vols = []
for i in image_data:
    x_vols.append(i[2])

# Y velocity increment.
y_vols = []
for i in image_data:
    y_vols.append(i[3])

# np array for convenience
xs = np.array(xs)
ys = np.array(ys)
x_vols = np.array(x_vols)
y_vols = np.array(y_vols)

# Make counter for the second problem.
counter = 0

# Fast forward
for i in range(10650):
    counter += 1
    xs += x_vols
    ys += y_vols

# Set up plotting area.
fig, ax = plt.subplots()
line, = ax.plot([], [], "o")

min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

ax.set_xlim((min_x - 1000, max_x + 1000))
ax.set_ylim((min_y - 1000, max_y + 1000))

# Animation initilization function
def init():
    line.set_data([], [])

    return line,

#  Animation function.
def animate(i, xs, ys, x_vols, y_vols, counter):

    counter += i

    xs += x_vols
    ys += y_vols

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)


    ax.set_xlim((min_x - (.1*min_x)), (max_x + (.1*max_x)))
    ax.set_ylim((min_y - (.1*max_y)), (max_y + (.1*max_y)))

    anchored_text = AnchoredText(counter, loc=2)
    ax.add_artist(anchored_text)

    line.set_data(xs, ys)

    return line,

fargs =(xs, ys, x_vols, y_vols, counter)

# Generate animation.
anim = animation.FuncAnimation(fig, animate, blit=False, interval=400,
                               repeat=True, init_func=init, fargs =fargs)
plt.show()

# Save a copy
anim.save('/home/will/Desktop/animation.gif', writer='imagemagick', fps=1)


