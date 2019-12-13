from aocd.models import Puzzle
import cv2
import numpy as np

puzzle = Puzzle(year=2019, day=11)
data = puzzle.input_data

intcode = data.split(',')
intcode = [int(i) for i in intcode]

def read_opcode(opcode, input, ap, rb, output=None, extend_mem=100000):
    # Extend memory
    ex_mem = [0]*extend_mem
    opcode.extend(ex_mem)
    # A variable to output indicating a '99'
    finished = False
    while True:
        # Track whether pointer has been changed by opcode
        ap_mod = False
        # Format opcode integer for parsing
        pm_inst = str(opcode[ap]).zfill(5)
        # Get opcode
        opc_info = int(pm_inst[-2:])
        # Get parameter modes
        fst_param_mode = int(pm_inst[-3])
        scd_param_mode = int(pm_inst[-4])
        thd_param_mode = int(pm_inst[-5])
        # Grab parameters
        address_1 = opcode[ap + 1]
        address_2 = opcode[ap + 2]
        address_3 = opcode[ap + 3]
        # Position mode
        if fst_param_mode == 0:
            val_1 = opcode[address_1]
        # Immediate mode
        elif fst_param_mode == 1:
            val_1 = address_1
        # Relative mode
        else:
            address_1 += rb
            val_1 = opcode[address_1]

        if scd_param_mode == 0:
            val_2 = opcode[address_2]
        elif scd_param_mode == 1:
            val_2 = address_2
        else:
            address_2 += rb
            val_2 = opcode[address_2]

        # So far this is only input so deal with relative mode
        if thd_param_mode == 2:
            address_3 += rb

        # Log
        #print(f'pointer: {ap} opcode: {opc_info} 1st mode: {fst_param_mode} 2nd mode: {scd_param_mode} 3rd mode: {thd_param_mode} va1_1: {val_1} val_2: {val_2}')

        # Perform operations based on code
        if opc_info == 1:
            new_value = val_1 + val_2
            opcode[address_3] = new_value
            ap += 4
        elif opc_info == 2:
            new_value = val_1 * val_2
            opcode[address_3] = new_value
            ap += 4
        elif opc_info == 3:
            opcode[address_1] = input
            ap += 2
        elif opc_info == 4:
            output = val_1
            print(f'output: {output}')
            ap += 2
            return output, opcode, ap, rb, finished
        elif opc_info == 5:
            if val_1 != 0:
                ap = val_2
                ap_mod = True
            if ap_mod == False:
                ap += 3
        elif opc_info == 6:
            if val_1 == 0:
                ap = val_2
                ap_mod = True
            if ap_mod == False:
                ap += 3
        elif opc_info == 7:
            if val_1 < val_2:
                store_val = 1
            else:
                store_val = 0
            opcode[address_3] = store_val
            ap += 4
        elif opc_info == 8:
            if val_1 == val_2:
                store_val = 1
            else:
                store_val = 0
            opcode[address_3] = store_val
            ap += 4
        elif opc_info == 9:
            rb += val_1
            ap += 2
        elif opc_info == 99:
            print('99')
            finished = True
            return output, opcode, ap, rb, finished

def robot(ship, color, next_direction, xcur, ycur, dir_cur):
    ship[ycur, xcur] = color
    if dir_cur == 'N':
        if next_direction == 0:
            xcur -= 1
            dir_cur = 'W'
        else:
            xcur += 1
            dir_cur = 'E'
    elif dir_cur == 'E':
        if next_direction == 0:
            ycur -= 1
            dir_cur = 'N'
        else:
            ycur += 1
            dir_cur = 'S'
    elif dir_cur == 'W':
        if next_direction == 0:
            ycur += 1
            dir_cur = 'S'
        else:
            ycur -= 1
            dir_cur = 'N'
    elif dir_cur == 'S':
        if next_direction == 0:
            xcur += 1
            dir_cur = 'E'
        else:
            xcur -= 1
            dir_cur = 'W'
    color_viewed = ship[ycur, xcur]
    return xcur, ycur, color_viewed, dir_cur

tiles_visited = []

ship = np.zeros((100,100), dtype=np.uint8)
out1, opc, ap, rb, finished = read_opcode(intcode.copy(), input=0, ap=0, rb=0, output=None, extend_mem=100000)
out2, opc, ap, rb, finished = read_opcode(opc, input=1, ap=ap, rb=rb, output=None, extend_mem=1)
xc, yc, cv, dc = robot(ship, color=out1, next_direction=out2, xcur=0, ycur=0, dir_cur='N')
print(f'cur x: {xc} cur y: {yc} cur view: {cv} dir_cur {dc}')
tiles_visited.append((xc,yc))

while not finished:
    tiles_visited.append((xc,yc))
    out1, opc, ap, rb, finished = read_opcode(opc, input=cv, ap=ap, rb=rb, output=None, extend_mem=1)
    if finished:
        break
    out2, opc, ap, rb, finished = read_opcode(opc, input=cv, ap=ap, rb=rb, output=None, extend_mem=1)
    xc, yc, cv, dc = robot(ship, color=out1, next_direction=out2, xcur=xc, ycur=yc, dir_cur=dc)
    print(f'cur x: {xc} cur y: {yc} cur view: {cv} dir_cur {dc}')

a_answer = (len(set(tiles_visited)))


ship = np.zeros((100,100), dtype=np.uint8)
out1, opc, ap, rb, finished = read_opcode(intcode.copy(), input=1, ap=0, rb=0, output=None, extend_mem=100000)
out2, opc, ap, rb, finished = read_opcode(opc, input=1, ap=ap, rb=rb, output=None, extend_mem=1)
xc, yc, cv, dc = robot(ship, color=out1, next_direction=out2, xcur=0, ycur=0, dir_cur='N')
print(f'cur x: {xc} cur y: {yc} cur view: {cv} dir_cur {dc}')
tiles_visited.append((xc,yc))

while not finished:
    out1, opc, ap, rb, finished = read_opcode(opc, input=cv, ap=ap, rb=rb, output=None, extend_mem=1)
    if finished:
        break
    out2, opc, ap, rb, finished = read_opcode(opc, input=cv, ap=ap, rb=rb, output=None, extend_mem=1)
    xc, yc, cv, dc = robot(ship, color=out1, next_direction=out2, xcur=xc, ycur=yc, dir_cur=dc)
    print(f'cur x: {xc} cur y: {yc} cur view: {cv} dir_cur {dc}')
    tiles_visited.append((xc,yc))

ship[ship == 1] = 255
ship = ship.astype(np.uint8)
cv2.imwrite('/home/will/advent_of_code/Advent-of-Code/2019/q11.png', ship)
b_answer = 'RJLFBUCU'

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
