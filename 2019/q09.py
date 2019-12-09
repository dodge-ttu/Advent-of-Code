from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=9)
data = puzzle.input_data

intcode = data.split(',')
intcode = [int(i) for i in intcode]

def read_opcode(opcode, input, ap, rb, grouped_input=False, output=None, extend_mem=10000):
    ex_mem = [0]*extend_mem
    opcode.extend(ex_mem)
    input_count = 0
    finished = False
    while True:
        ap_mod = False
        pm_inst = str(opcode[ap]).zfill(5)
        opc_info = int(pm_inst[-2:])
        fst_param_mode = int(pm_inst[-3])
        scd_param_mode = int(pm_inst[-4])
        thd_param_mode = int(pm_inst[-5])
        #print(fst_param_mode, scd_param_mode, thd_param_mode)
        address_1 = opcode[ap + 1]
        address_2 = opcode[ap + 2]
        address_3 = opcode[ap + 3]
        if fst_param_mode == 0:
            val_1 = opcode[address_1]
        elif fst_param_mode == 1:
            val_1 = address_1
        else:
            val_1 = opcode[address_1 + rb]
        if scd_param_mode == 0:
            val_2 = opcode[address_2]
        elif scd_param_mode == 1:
            val_2 = address_2
        else:
            val_2 = opcode[address_2 + rb]
        if thd_param_mode == 0:
            val_3 = opcode[address_3]
        elif thd_param_mode == 1:
            val_3 = address_3
        else:
            val_3 = opcode[address_3 + rb]
        if opc_info == 1:
            new_value = val_1 + val_2
            opcode[val_3] = new_value
            ap += 4
        elif opc_info == 2:
            new_value = val_1 * val_2
            opcode[val_3] = new_value
            ap += 4
        elif opc_info == 3:
            if grouped_input:
                if input_count == 0:
                    opcode[val_1] = input[0]
                    input_count += 1
                else:
                    opcode[val_1] = input[1]
            else:
                opcode[val_1] = input
            ap += 2
        elif opc_info == 4:
            if fst_param_mode == 1:
                output = val_1
            else:
                output = opcode[val_1]
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
            opcode[val_3] = store_val
            ap += 4
        elif opc_info == 8:
            if val_1 == val_2:
                store_val = 1
            else:
                store_val = 0
            opcode[val_3] = store_val
            ap += 4
        elif opc_info == 9:
            rb += val_1
            ap += 2
        elif opc_info == 99:
            print('99')
            finished = True
            return output, opcode, ap, rb, finished
        
intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

sig, oc, ap, rb, _ = read_opcode(intcode.copy(), input=9, ap=0, rb=0, grouped_input=False)

finished = False

while finished == False:
    sig, oc, ap, rb, finished = read_opcode(oc, input=1, ap=ap, rb=rb, grouped_input=False)

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

