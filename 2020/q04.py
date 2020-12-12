from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=4)
data_rough = puzzle.input_data.splitlines()
data_ls = []
passport = []
for (idx,s) in enumerate(data_rough,1):
    if s == '':
        data_ls.append(passport)
        passport = []
    elif idx == len(data_rough):
        data_ls.append(passport) # Deal with last field set
    else:
        passport.append(s)
DATA = []
for passport in data_ls:
    passport = [field.split(' ') for field in passport]
    individual_kv_pairs = []
    for fields in passport:
        for field in fields:
            (k, v) = field.split(':')
            individual_kv_pairs.append((k, v))
    passport = dict(individual_kv_pairs)
    DATA.append(passport)

# Part A
def count_valid_passports(data):
    count = 0
    for passport in data:
        if len(passport) == 8:
            count += 1
        elif (len(passport) == 7) and ('cid' not in passport):
            count += 1
    return count

a_answer = count_valid_passports(DATA)

# Part B
def fix_passports(data):
    count = 0
    for passport in data:
        if len(passport) > 6:
            field_checks = 0
            byr = passport.get('byr')
            if byr:
                if 1920 <= int(byr) <= 2002:
                    field_checks+=1
            iyr = passport.get('iyr')
            if iyr:
                if 2010 <= int(iyr) <= 2020:
                    field_checks+=1
            eyr = passport.get('eyr')
            if eyr:
                if 2020 <= int(eyr) <= 2030:
                    field_checks+=1
            hgt = passport.get('hgt')
            if hgt:
                if 'cm' in passport['hgt']:
                    if 150 <= int(hgt[:-2]) <=193:
                        field_checks+=1
                elif 'in' in passport['hgt']:
                    if 59 <= int(hgt[:-2]) <= 76:
                        field_checks+=1
            hcl = passport.get('hcl')
            if hcl:
                if hcl[0] == '#':
                    good_chars = True
                    for l in hcl[1:]:
                        if l.isdigit():
                            good_chars = 0 <= int(l) <= 9
                        elif l.isalpha():
                            good_chars = l in 'abcdef'
                    if good_chars:
                        field_checks+=1
            ecl = passport.get('ecl')
            if ecl:
                if ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                    field_checks+=1
            pid = passport.get('pid')
            if pid:
                if (len(pid) == 9) and (pid.isdigit()):
                    field_checks+=1
            if field_checks > 6:
                count += 1
    return count

b_answer = fix_passports(DATA)

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
