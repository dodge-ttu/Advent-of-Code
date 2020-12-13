from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=5)
DATA = puzzle.input_data.splitlines()
#DATA= ['BBFFBBFRLL']

# Part A
def max_seat_id(data):
    seat_ids = []
    for seat_map in data:
        nr = 128
        rows = [i for i in range(nr)]
        for l in seat_map[:-3]:
            nr = int(nr*.5)
            if l == 'F':
                rows = rows[:nr]
            if l == 'B':
                rows = rows[nr:]
        nc = 8
        cols = [i for i in range(nc)]
        for l in seat_map[-3:]:
            nc = int(nc*.5)
            if l == 'L':
                cols = cols[:nc]
            if l == 'R':
                cols = cols[nc:]
        seat_id = rows[0]*8 + cols[0]
        seat_ids.append(seat_id)
        max_seat_id = max(seat_ids)
    return max_seat_id

a_answer = max_seat_id(DATA)

# Part B
def my_seat_id(data):
    seat_ids = []
    for seat_map in data:
        nr = 128
        rows = [i for i in range(nr)]
        for l in seat_map[:-3]:
            nr = int(nr*.5)
            if l == 'F':
                rows = rows[:nr]
            if l == 'B':
                rows = rows[nr:]
        nc = 8
        cols = [i for i in range(nc)]
        for l in seat_map[-3:]:
            nc = int(nc*.5)
            if l == 'L':
                cols = cols[:nc]
            if l == 'R':
                cols = cols[nc:]
        seat_id = rows[0]*8 + cols[0]
        seat_ids.append(seat_id)
    min_seat_id = min(seat_ids)
    max_seat_id = max(seat_ids)
    seat_ids_with_missing = set(list(range(min_seat_id, max_seat_id+1)))
    missing = list(seat_ids_with_missing - set(seat_ids))[0]
    return missing

b_answer = my_seat_id(DATA)

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
