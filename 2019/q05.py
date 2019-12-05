from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=5)
data = puzzle.input_data
diagnostic_program = [int(s) for s in data.split(',')]

# diagnostic_program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

def read_opcode(opcode, input):
    ap = 0
    while True:
        ap_mod = False
        pm_inst = str(opcode[ap]).zfill(5)
        opc_info = int(pm_inst[-2:])
        fst_param_mode = int(pm_inst[-3])
        scd_param_mode = int(pm_inst[-4])
        try:
            address_1 = opcode[ap + 1]
            address_2 = opcode[ap + 2]
            address_3 = opcode[ap + 3]
        except:
            print('done')
        #print(pm_inst, address_1, address_2, address_3)
        if opc_info in {1,2,5,6,7,8}:
            val_1 = opcode[address_1] if fst_param_mode == 0 else address_1
            val_2 = opcode[address_2] if scd_param_mode == 0 else address_2
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
            #print(output)
            ap += 2
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
        elif opc_info == 99:
            break
    if output:
        return output

a_answer = read_opcode(opcode=diagnostic_program.copy(), input=1)
b_answer = read_opcode(opcode=diagnostic_program.copy(), input=5)

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
