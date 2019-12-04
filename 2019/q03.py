from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=3)
data = puzzle.input_data

wires = data.split('\n')
wires = [wire.split(',') for wire in wires]

wire_span_coords = []

for wire_span_info in wires:
    x_pos_old = 0
    y_pos_old = 0
    x_pos_new = 0
    y_pos_new = 0
    a_wires_spans = []
    for span in wire_span_info:
        direction = span[0]
        distance = int(span[1:])
        if direction == 'R':
            x_pos_new += distance
        elif direction == 'L':
            x_pos_new -= distance
        elif direction == 'U':
            y_pos_new += distance
        elif direction == 'D':
            y_pos_new -= distance
        a_wires_spans.append(((x_pos_old, y_pos_old), (x_pos_new, y_pos_new)))
        x_pos_old = x_pos_new
        y_pos_old = y_pos_new
    wire_span_coords.append(a_wires_spans)

# Create a list of ordered pairs representing all points on wire
all_points_on_wires = []

for wire_coords in wire_span_coords:
    all_points_on_this_wire = []
    for ((x1,y1),(x2,y2)) in wire_coords:
        if x1 < x2:
            xx = [i for i in range(x1, x2, 1)]
            yy = [y1] * len(xx)
        if x2 < x1:
            xx = [i for i in range(x1, x2,-1)]
            yy = [y1] * len(xx)
        if y1 < y2:
            yy = [i for i in range(y1, y2, 1)]
            xx = [x1] * len(yy)
        if y2 < y1:
            yy = [i for i in range(y1, y2, -1)]
            xx = [x1] * len(yy)
        xxyy = [(x,y) for x,y in zip(xx,yy)]
        all_points_on_this_wire.extend(xxyy)
    all_points_on_wires.append(all_points_on_this_wire)

all_points_on_wires_sets = [set(pts_on_wire) for pts_on_wire in all_points_on_wires]

wire_1_ls = all_points_on_wires[0]
wire_2_ls = all_points_on_wires[1]
wire_1_set = all_points_on_wires_sets[0]
wire_2_set = all_points_on_wires_sets[1]

intersections = wire_1_set.intersection(wire_2_set)
intersections = [s for s in intersections if s != (0,0)]

# Part A: Find the intersection closest to the origin.
intersections_distances = []
for (x,y) in intersections:
    intersections_distances.append(((x,y), abs(x)+abs(y)))

# Part B: Find the intersection with the shortest pieces of wire (fewest steps).
intersection_wire_lengths = []
for an_intersect in intersections:
    wire_one_length = wire_1_ls.index(an_intersect)
    wire_two_length = wire_2_ls.index(an_intersect)
    intersection_wire_lengths.append((an_intersect, wire_one_length+wire_two_length))

a_answer = min(intersections_distances, key=lambda x: x[1])
b_answer = min(intersection_wire_lengths, key=lambda x: x[1])

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
