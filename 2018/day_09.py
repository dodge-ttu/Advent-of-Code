import timeit
import itertools
import math


#region Problem 1
#
# You talk to the Elves while you wait for your navigation system to initialize. To pass the time, they introduce
# you to their favorite marble game.
#
# The Elves play this game by taking turns arranging the marbles in a circle according to very particular rules.
# The marbles are numbered starting with 0 and increasing by 1 until every marble has a number.
#
# First, the marble numbered 0 is placed in the circle. At this point, while it contains only a single marble,
# it is still a circle: the marble is both clockwise from itself and counter-clockwise from itself. This marble
# is designated the current marble.
#
# Then, each Elf takes a turn placing the lowest-numbered remaining marble into the circle between the marbles
# that are 1 and 2 marbles clockwise of the current marble. (When the circle is large enough, this means that
# there is one marble between the marble that was just placed and the current marble.) The marble that was just
# placed then becomes the current marble.
#
# However, if the marble that is about to be placed has a number which is a multiple of 23, something entirely
# different happens. First, the current player keeps the marble they would have placed, adding it to their score.
# In addition, the marble 7 marbles counter-clockwise from the current marble is removed from the circle and also
# added to the current player's score. The marble located immediately clockwise of the marble that was removed
# becomes the new current marble.
#
# For example, suppose there are 9 players. After the marble with value 0 is placed in the middle, each player
# (shown in square brackets) takes a turn. The result of each of those turns would produce circles of marbles like
# this, where clockwise is to the right and the resulting current marble is in parentheses:
#
# [-] (0)
# [1]  0 (1)
# [2]  0 (2) 1
# [3]  0  2  1 (3)
# [4]  0 (4) 2  1  3
# [5]  0  4  2 (5) 1  3
# [6]  0  4  2  5  1 (6) 3
# [7]  0  4  2  5  1  6  3 (7)
# [8]  0 (8) 4  2  5  1  6  3  7
# [9]  0  8  4 (9) 2  5  1  6  3  7
# [1]  0  8  4  9  2(10) 5  1  6  3  7
# [2]  0  8  4  9  2 10  5(11) 1  6  3  7
# [3]  0  8  4  9  2 10  5 11  1(12) 6  3  7
# [4]  0  8  4  9  2 10  5 11  1 12  6(13) 3  7
# [5]  0  8  4  9  2 10  5 11  1 12  6 13  3(14) 7
# [6]  0  8  4  9  2 10  5 11  1 12  6 13  3 14  7(15)
# [7]  0(16) 8  4  9  2 10  5 11  1 12  6 13  3 14  7 15
# [8]  0 16  8(17) 4  9  2 10  5 11  1 12  6 13  3 14  7 15
# [9]  0 16  8 17  4(18) 9  2 10  5 11  1 12  6 13  3 14  7 15
# [1]  0 16  8 17  4 18  9(19) 2 10  5 11  1 12  6 13  3 14  7 15
# [2]  0 16  8 17  4 18  9 19  2(20)10  5 11  1 12  6 13  3 14  7 15
# [3]  0 16  8 17  4 18  9 19  2 20 10(21) 5 11  1 12  6 13  3 14  7 15
# [4]  0 16  8 17  4 18  9 19  2 20 10 21  5(22)11  1 12  6 13  3 14  7 15
# [5]  0 16  8 17  4 18(19) 2 20 10 21  5 22 11  1 12  6 13  3 14  7 15
# [6]  0 16  8 17  4 18 19  2(24)20 10 21  5 22 11  1 12  6 13  3 14  7 15
# [7]  0 16  8 17  4 18 19  2 24 20(25)10 21  5 22 11  1 12  6 13  3 14  7 15
# The goal is to be the player with the highest score after the last marble is used up. Assuming the example above ends after the marble numbered 25, the winning score is 23+9=32 (because player 5 kept marble 23 and removed marble 9, while no other player got any points in this very short example game).
#
# Here are a few more examples:
#
# 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# 17 players; last marble is worth 1104 points: high score is 2764
# 21 players; last marble is worth 6111 points: high score is 54718
# 30 players; last marble is worth 5807 points: high score is 37305
#
# What is the winning Elf's score?
#
#endregion

### Test cases:

p1_a = ([9, 25], 32)
p1_b = ([10, 1618], 8317)
p1_c = ([13, 7999], 146373)
p1_d = ([17, 1104], 2764)
p1_e = ([21, 6111], 54718)
p1_f = ([30, 5807], 37305)

p1_test_cases = {
    "p1_a":p1_a,
    "p1_b":p1_b,
    "p1_c":p1_c,
    "p1_d":p1_d,
    "p1_e":p1_e,
}

### Answers:

# The placing of an individual marble is a pattern:
#
# 1,1,3,1,3,5,7,1,3,5,7,9,11,13,15,1,3............
#
# Looking that up on OEIS one finds the following series:
#
# https://oeis.org/A006257
#
# Described with the formula: 2*(n-2**int(math.log(n, 2)))+1

def p1answer1(ls):

    def find_insertion_point(integer):
        if integer == 0:
            return 1
        else:
            loc = 2*(integer-2**int(math.log(integer, 2)))+1
            return loc

    players = ls[0]
    last_pnts = ls[1]

    game_board = [0]
    other_loc = 0

    score_dict = {}

    for i in range(1, players + 1):
        score_dict[i] = 0

    for i in range(1, last_pnts):
        print(game_board)
        insertion_location = find_insertion_point(i)
        insertion_location = insertion_location - other_loc

        current_player = (i % players) +1

        if i % 23 == 0:
            other_loc = (insertion_location - 9)
            print(other_loc)
            print(insertion_location)
            plus_removal = game_board.pop(other_loc)
            print(plus_removal)
            score_dict[current_player] += (i + plus_removal)
            print(i)
            other_loc += 7

        else:
            game_board.insert(insertion_location, i)






    max_score = max(score_dict.items(), key=lambda x: x[1])

    return max_score[1]

p1answers = {
    "p1answer1":p1answer1,
}

### Problem 1 tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))



#region Problem 2
#
#
#
#endregion

### Test cases:



### Answers:

def p2answer1(ls):
    pass

p2answers = {
    "p2answer1":p2answer1,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))



####### Official Input Data #######

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_01_input.txt"

with open(file_path, newline='') as csv_file:
    raw_data = csv.reader(csv_file, delimiter=" ", quoting=csv.QUOTE_NONNUMERIC)
    data = []
    for i in list(raw_data):
        data.extend(i)



####### Performance  #######

# Performance testing on official data.

def time_with_official_data(problem_number, answer_dict, loops=1):
    for (answer_name, answer) in answer_dict.items():
        time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)
