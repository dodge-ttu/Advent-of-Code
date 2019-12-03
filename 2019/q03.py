from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=3)
data = puzzle.input_data

wires = data.split('\n')
wires = [wire.split(',') for wire in wires]

# test =[
#     ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
#     ['U62','R66','U55','R34','D71','R55','D58','R83']
# ]
# wires = test

# test = [
#     ['R8','U5','L5','D3'],
#     ['U7','R6','D4','L4']
# ]
# wires=test

# Create coordinates representing wire segments
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

# Part B: Find the intersection with the shorted pieces of wire (fewest steps).
intersection_wire_lengths = []
for an_intersect in intersections:
    wire_one_length = wire_1_ls.index(an_intersect)
    wire_two_length = wire_2_ls.index(an_intersect)
    intersection_wire_lengths.append((an_intersect, wire_one_length+wire_two_length))

print(f'answer a: {min(intersections_distances, key=lambda x: x[1])}')
print(f'answer b: {min(intersection_wire_lengths, key=lambda x: x[1])}')
print(f'[INFO] Puzzle Title: {puzzle.title}')
print(f'[INFO] Part A answer: {puzzle.answer_a}')
print(f'[INFO] Part B answer: {puzzle.answer_b}')
