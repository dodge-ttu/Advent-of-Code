import timeit
import sys
sys.setrecursionlimit(5000)

#region Problem 1
#
# The tree is made up of nodes; a single, outermost node forms the tree's root, and it contains all other nodes in
# the tree (or contains nodes that contain nodes, and so on).
#
# Specifically, a node consists of:
#
# A header, which is always exactly two numbers:
# The quantity of child nodes.
# The quantity
# of metadata entries.
# Zero or more child nodes (as specified in the header).
# One or more metadata entries (as specified in the header).
# Each child node is itself a node that has its own header, child nodes, and metadata. For example:
#
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----
# In this example, each node of the tree is also marked with an underline starting with a letter for easier
# identification. In it, there are four nodes:
#
# A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
# B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
# C, which has 1 child node (D) and 1 metadata entry (2).
# D, which has 0 child nodes and 1 metadata entry (99).

# The first check done on the license file is to simply add up all of the metadata entries. In this example,
# that sum is 1+1+2+10+11+12+2+99=138.
#
#endregion

### Test cases:

p1_a = ([2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2],138)

p1_test_cases = {
    "p1_a":p1_a,
}

### Answers:

# Passes test case breaks on actual input.
def p1answer1(ls, *args, **kwargs):

    def build_tree(ls, tree=None,  node_ID = 0, *args, **kwargs):

        if not ls:
            return tree

        children = ls.pop(0)
        metadata = ls.pop(0)

        if children == 0:
            meta_values = []
            for i in range(metadata):
                value = ls.pop(0)
                meta_values.append(value)
            tree[node_ID] = meta_values

            return build_tree(ls, tree=tree, node_ID= node_ID+1)

        else:
            meta_values = []
            for i in range(metadata):
                value = ls.pop(-1)
                meta_values.append(value)
            tree [node_ID] = meta_values

            return build_tree(ls, tree=tree, node_ID= node_ID+1)

        return build_tree(ls, tree={})

# Getting absolutely nowhere.... must try something new
# https://stackoverflow.com/questions/5369723/multi-level-defaultdict-with-variable-depth/8702435#8702435
# https://stackoverflow.com/a/28015122
# https://stackoverflow.com/a/2358075
# https://stackoverflow.com/a/14920967
# https://stackoverflow.com/a/2482610/
# http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
# http://interactivepython.org/courselib/static/pythonds/index.html
# http://interactivepython.org/runestone/static/pythonds/Trees/VocabularyandDefinitions.html
# https://stackoverflow.com/a/14015526


def p1answer2(ls, *args, **kwargs):

    class Node:
        def __init__(self, key, parent=None, numChildren=None, numMeta=None):
            self.key = key
            self.parent = parent
            self.numChildren = numChildren
            self.numMeta = numMeta
            self.metadata = []
            self.children = []
            self.children_copy = []
            self.visited = False

        def add_child(self, key):
            leaf = Node(key)
            leaf.parent = self
            self.children.append(leaf)

    letters = (str(i) for i in range(10000))

    root = Node(key=next(letters))
    root.parent = Node("root")
    root.parent.visited = True
    root.parent.children.append(root)

    def build_tree(current_node, ls, asum=0):

        if not ls:
            return current_node, asum

        if current_node.key == "root" and ls:
            current_node = current_node.children[0]

            return build_tree(current_node, ls)

        if current_node.visited == False:
            num_child = ls.pop(0)
            metadata = ls.pop(0)

            current_node.numChildren = num_child
            current_node.numMeta = metadata
            current_node.visited = True

            if current_node.numChildren > 0:
                for i in range(current_node.numChildren):
                    current_node.add_child(next(letters))

                if current_node.parent == "root":
                    root.children_copy == root.children.copy()

                current_node = current_node.children.pop(0)

                return build_tree(current_node, ls, asum)

            elif current_node.numChildren == 0:
                meta_ls = []
                for i in range(current_node.numMeta):
                    value = ls.pop(0)
                    meta_ls.append(value)

                current_node.metadata = meta_ls

                asum += sum(meta_ls)

                if current_node.parent.children:
                    current_node = current_node.parent.children.pop(0)
                else:
                    current_node = current_node.parent

                return build_tree(current_node, ls, asum)

        elif current_node.visited == True and ls:
            meta_ls = []
            for i in range(current_node.numMeta):
                value = ls.pop(0)
                meta_ls.append(value)

            current_node.metadata = meta_ls

            asum += sum(meta_ls)

            if current_node.parent and current_node.parent != "root":
                current_node = current_node.parent

            if current_node.parent and current_node.parent == "root":
                current_node = current_node.children[0]

            elif current_node.children:
                current_node = current_node.children.pop(0)

            return build_tree(current_node, ls, asum)

    tree, asum = build_tree(root, ls)

    return asum

p1answers = {
    "p1answer1":p1answer1,
    "p1answer2":p1answer2,
}

### Problem 1 tests:

for (answer_name, answer) in p1answers.items():
    for test_name, (test,sol) in p1_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 1] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 1] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 1] Test: FAIL, Function: p1answer1 Input: [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
# [Problem 1] Test: PASS, Function: p1answer2 Input: []

#region Problem 2
#
# The second check is slightly more complicated: you need to find the value of the root node (A in the example above).
#
# The value of a node depends on whether it has child nodes.
#
# If a node has no child nodes, its value is the sum of its metadata entries. So, the value of node B is 10+11+12=33,
# and the value of node D is 99.
#
# However, if a node does have child nodes, the metadata entries become indexes which refer to those child nodes.
# A metadata entry of 1 refers to the first child node, 2 to the second, 3 to the third, and so on. The value of
# this node is the sum of the values of the child nodes referenced by the metadata entries. If a referenced child
# node does not exist, that reference is skipped. A child node can be referenced multiple time and counts each time
# it is referenced. A metadata entry of 0 does not refer to any child node.
#
# For example, again using the above nodes:
#
# Node C has one metadata entry, 2. Because node C has only one child node, 2 references a child node which does
# not exist, and so the value of node C is 0.
#
# Node A has three metadata entries: 1, 1, and 2. The 1 references node A's first child node, B, and the 2 references
# node A's second child node, C. Because node B has a value of 33 and node C has a value of 0, the value of node
# A is 33+33+0=66.
# So, in this example, the value of the root node is 66.
#
# What is the value of the root node?
#
#endregion

### Test cases:

p2_a = ([2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2],66)

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(ls, *args, **kwargs):

    class Node:
        def __init__(self, key, parent=None, numChildren=None, numMeta=None):
            self.key = key
            self.parent = parent
            self.numChildren = numChildren
            self.numMeta = numMeta
            self.metadata = []
            self.children = []
            self.children_copy = []
            self.visited = False

        def add_child(self, key):
            leaf = Node(key)
            leaf.parent = self
            self.children.append(leaf)
            self.children_copy.append(leaf)

    letters = (i for i in range(10000))

    root = Node(key=next(letters))
    root.parent = Node("root")
    root.parent.visited = True
    root.parent.children.append(root)

    master_dict = {}

    def build_tree(current_node, ls, asum=0):

        if not ls:
            return current_node, asum

        if current_node.key == "root" and ls:
            current_node = current_node.children[0]

            return build_tree(current_node, ls)

        if current_node.visited == False:
            num_child = ls.pop(0)
            metadata = ls.pop(0)

            current_node.numChildren = num_child
            current_node.numMeta = metadata
            current_node.visited = True

            if current_node.numChildren > 0:
                for i in range(current_node.numChildren):
                    current_node.add_child(next(letters))

                if current_node.parent == "root":
                    root.children_copy == root.children.copy()

                current_node = current_node.children.pop(0)

                return build_tree(current_node, ls, asum)

            elif current_node.numChildren == 0:
                meta_ls = []
                for i in range(current_node.numMeta):
                    value = ls.pop(0)
                    meta_ls.append(value)

                current_node.metadata = meta_ls

                asum += sum(meta_ls)

                aa = [i.key for i in current_node.children_copy]
                aa_rent = current_node.parent.key

                master_dict[current_node.key] = (current_node.metadata, aa, aa_rent)

                if current_node.parent.children:
                    current_node = current_node.parent.children.pop(0)
                else:
                    current_node = current_node.parent

                return build_tree(current_node, ls, asum)

        elif current_node.visited == True and ls:
            meta_ls = []
            for i in range(current_node.numMeta):
                value = ls.pop(0)
                meta_ls.append(value)

            current_node.metadata = meta_ls

            aa = [i.key for i in current_node.children_copy]
            aa_rent = current_node.parent.key

            master_dict[current_node.key] = (current_node.metadata, aa, aa_rent)

            asum += sum(meta_ls)

            if current_node.parent and current_node.parent != "root":
                current_node = current_node.parent

            if current_node.parent and current_node.parent == "root":
                current_node = current_node.children[0]

            elif current_node.children:
                current_node = current_node.children.pop(0)

            return build_tree(current_node, ls, asum)

    tree, asum = build_tree(root, ls)

    cleaner_dict = {}

    for (k, v) in master_dict.items():

        if not v[1]:
            asum = sum(v[0])
            cleaner_dict[k] = [[], asum, v[2], []]

        else:
            kids_that_count = []
            for i in v[0]:
                try:
                    a_kid = v[1][i - 1]
                    kids_that_count.append(a_kid)
                except:
                    pass
            cleaner_dict[k] = [kids_that_count, 0, v[2], []]

    root = cleaner_dict[0]

    def count_node(current_node, node_sum=0):

        if not current_node[0] and current_node[2] == "root":
            return node_sum

        elif not current_node[0]:
            this_nodes_sum = current_node[1]
            node_sum += this_nodes_sum
            parent = cleaner_dict[current_node[2]]
            parent[1] += this_nodes_sum

            current_node = parent

            return count_node(current_node, node_sum)

        else:
            next_key = current_node[0].pop(0)
            current_node[3].append(next_key)
            next_child = cleaner_dict[next_key]
            current_node = next_child

            return count_node(current_node, node_sum)

    node_sum = count_node(root)

    return node_sum

def p2answer2(*args, **kwargs):
    pass

p2answers = {
    "p2answer1":p2answer1,
    "p2answer2":p2answer2,
}

### Problem 2 tests:

for (answer_name, answer) in p2answers.items():
    for test_name, (test,sol) in p2_test_cases.items():
        if (answer(test) == sol):
            print("[Problem 2] Test: PASS, Function: {0} Input: {1}".format(answer_name, test))
        else:
            print("[Problem 2] Test: FAIL, Function: {0} Input: {1}".format(answer_name, test))

# [Problem 2] Test: PASS, Function: p2answer1 Input: []
# [Problem 2] Test: FAIL, Function: p2answer2 Input: []


####### Official Input Data #######

### CSV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_08_input.txt"

with open(file_path) as my_file:
    raw_data = my_file.read().split()
    data = []
    for i in raw_data:
        data.append(int(i))


####### Performance  #######

def time_with_official_data(problem_number, answer_dict, loops=1, testing=False, *args, **kwargs):
    for (answer_name, answer) in answer_dict.items():
        if not testing:
            time = timeit.timeit("{0}(data)".format(answer_name), globals=globals(), number=loops)
        else:
            time = timeit.timeit("{0}(data, testing=False)".format(answer_name), globals=globals(), number=loops)

        time = round(time, 5)
        print("[Problem {0}] Time: {1} seconds on {2} loops, Function: {3}".format(problem_number,time,loops,answer_name))

time_with_official_data(problem_number=1, answer_dict=p1answers, loops=1)

# remake actual data as it gets empty from popping

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_08_input.txt"

with open(file_path) as my_file:
    raw_data = my_file.read().split()
    data = []
    for i in raw_data:
        data.append(int(i))

time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

# [Problem 1] Time: 0.0 seconds on 1 loops, Function: p1answer1
# [Problem 1] Time: 0.03869 seconds on 1 loops, Function: p1answer2
# [Problem 2] Time: 0.03899 seconds on 1 loops, Function: p2answer1
# [Problem 2] Time: 0.0 seconds on 1 loops, Function: p2answer2