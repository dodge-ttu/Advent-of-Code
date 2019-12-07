from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=6)
data = puzzle.input_data.split('\n')

class Node:
    def __init__(self, key=None):
        self.L = None
        self.R = None
        self.V = key
        self.level = 0
        self.parent = None

#data = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
data = [tuple(s.split(')')) for s in data]
# Everyone is a child but not everyone is a parent :(
parent_keys = {t[0]:[] for t in data}
children_keys = {t[1]:t[0] for t in data}
children_to_be_created = set(children_keys.keys())

for (p,c) in data:
    parent_keys[p].append(c)

tree = Node(key='COM')
n = tree
children = None
while children_to_be_created:
    value = n.V
    print(value, n.level)
    # Find Children
    if value in parent_keys:
        children = parent_keys[value]
        if len(children) != 0:
            # Initialize child nodes
            if not n.L:
                try:
                    next_child = parent_keys[value].pop(0)
                    children_to_be_created.remove(next_child)
                    n.L = Node(key=next_child)
                    n.L.parent = n
                    n.L.level = n.level + 1
                    n = n.L
                except:
                    n = n.parent
            elif not n.R:
                try:
                    next_child = parent_keys[value].pop(0)
                    children_to_be_created.remove(next_child)
                    n.R = Node(key=next_child)
                    n.R.parent = n
                    n.R.level = n.level + 1
                    n = n.R
                except:
                    n = n.parent
        else:
            print(children)
            print(n.parent.V)
            n = n.parent
    else:
        print('No children, going to parent')
        try:
            print(n.parent)
            n = n.parent
            print(f'node now parent node: {n.V}')
        except:
            print("Orphan child node?")

def inorder_count_all_orbits(node, count=0):
    if node:
        if node.L:
            count = inorder_count_all_orbits(node.L, count=count)
        if node.R:
            count = inorder_count_all_orbits(node.R, count=count)
    return count + node.level

a_answer = inorder_count_all_orbits(tree)

def me_to_santa(node, path, k):
    if node is None:
        return False

    path.append(node.V)

    if node.V == k:
        return True

    if ((node.L != None) and me_to_santa(node.L, path, k) or
        ((node.R != None) and me_to_santa(node.R, path, k))):
        return True

    path.pop()
    return False

def distance(node, data1, data2):
    if node:
        path1 = []
        me_to_santa(node, path1, data1)

        path2 = []
        me_to_santa(node, path2, data2)

        i=0
        while i<len(path1) and i <len(path2):
            if path1[i] != path2[i]:
                break
            i = i+1

        return (len(path1) + len(path2) - 2*i)
    else:
        return 0

b_answer = distance(tree, 'YOU', 'SAN') - 2

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
