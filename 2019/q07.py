from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=7)
data = puzzle.input_data.split(',')

def read_opcode(opcode, input, ap, grouped_input=False, output=None):
    input_count = 0
    finished = False
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
            if grouped_input:
                if input_count == 0:
                    opcode[address_1] = input[0]
                    input_count += 1
                else:
                    opcode[address_1] = input[1]
            else:
                opcode[address_1] = input
            ap += 2
        elif opc_info == 4:
            output = opcode[address_1]
            ap += 2
            return output, opcode, ap, finished
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
            finished = True
            return output, opcode, ap, finished

amp_control_software = [int(i) for i in data]

# a_test = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
# 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]


thrust_outputs = []
for i in range(0,44444):
    program = amp_control_software.copy()
    #program = a_test
    phase_sequence = [int(i) for i in str(i).zfill(5)]
    phase_sequence = [i for i in phase_sequence if i <= 4]
    if len(set(phase_sequence)) == 5:
        #print(i)
        #(A,B,C,D,E) = [1,0,4,3,2]
        (A,B,C,D,E) = phase_sequence.copy()
        a_sig, a_oc, _, _ = read_opcode(program.copy(), input=[A,0], ap=0, grouped_input=True)
        b_sig, b_oc, _, _ = read_opcode(program.copy(), input=[B,a_sig], ap=0, grouped_input=True)
        c_sig, c_oc, _, _ = read_opcode(program.copy(), input=[C,b_sig], ap=0, grouped_input=True)
        d_sig, d_oc, _, _ = read_opcode(program.copy(), input=[D,c_sig], ap=0, grouped_input=True)
        thrust_sig, e_oc, _, finished_e = read_opcode(program.copy(), input=[E,d_sig], ap=0, grouped_input=True)
        thrust_outputs.append((thrust_sig, i))

a_answer = max(thrust_outputs, key=lambda x: x[0])
print(a_answer)

amp_control_software = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

thrust_signals = []

for i in range(55555,99999):
    program = amp_control_software.copy()
    phase_sequence = [int(i) for i in str(i).zfill(5)]
    phase_sequence = [i for i in phase_sequence if i >= 5]
    if len(set(phase_sequence)) == 5:
        print(i)
        (A,B,C,D,E) = [9,8,7,6,5]
        a_ap = 0
        b_ap = 0
        c_ap = 0
        d_ap = 0
        e_ap = 0
        a_oc = program.copy()
        b_oc = program.copy()
        c_oc = program.copy()
        d_oc = program.copy()
        e_oc = program.copy()

        a_sig, a_oc, a_ap, _ = read_opcode(a_oc, input=A, ap=a_ap)
        print('a', a_sig, a_ap, _)
        b_sig, b_oc, b_ap, _ = read_opcode(b_oc, input=B, ap=b_ap)
        print('b', b_sig, b_ap, _)
        c_sig, c_oc, c_ap, _ = read_opcode(c_oc, input=C, ap=c_ap)
        print('c', c_sig, c_ap, _)
        d_sig, d_oc, d_ap, _ = read_opcode(d_oc, input=D,  ap=d_ap)
        print('d', d_sig, d_ap, _)
        thrust_sig, e_oc, e_ap, finished_e = read_opcode(e_oc, input=E, ap=e_ap)
        print('e', thrust_sig, e_ap, finished_e)

        thrust_sig = 0

        while finished_e == False:
            thrust_signals.append(thrust_sig)
            a_sig, a_oc, a_ap, _ = read_opcode(a_oc, input=thrust_sig, ap=a_ap)
            print('a', a_sig, a_ap, _)
            b_sig, b_oc, b_ap, _ = read_opcode(b_oc, input=a_sig, ap=b_ap)
            print('b', b_sig, b_ap, _)
            c_sig, c_oc, c_ap, _ = read_opcode(c_oc, input=b_sig, ap=c_ap)
            print('c', c_sig, c_ap, _)
            d_sig, d_oc, d_ap, _ = read_opcode(d_oc, input=c_sig, ap=d_ap)
            print('d', d_sig, d_ap, _)
            thrust_sig, e_oc, e_ap, finished_e = read_opcode(e_oc, input=d_sig, ap=e_ap)
            print('e', thrust_sig, e_ap, finished_e)

print(max(thrust_signals))


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



