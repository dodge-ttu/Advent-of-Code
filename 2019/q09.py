from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=9)
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
            output = opcode[address_1]
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

#intcode = [1102,34915192,34915192,7,4,7,99,0]

a_sig, oc, ap, rb, _ = read_opcode(intcode.copy(), input=1, ap=0, rb=0)
a_answer = a_sig

b_sig, oc, ap, rb, _ = read_opcode(intcode.copy(), input=2, ap=0, rb=0)
b_answer = b_sig

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

