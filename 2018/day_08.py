import timeit

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

p1_b = ([1,1,0,1,99,2], 101)

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
            print(asum)
            return current_node, asum

        if current_node.key == "root" and ls:
            print("look root")
            current_node = current_node.children[0]

            return build_tree(current_node, ls)

        if current_node.visited == False:
            print("here")
            print(current_node.key)
            print(current_node.visited)
            num_child = ls.pop(0)
            metadata = ls.pop(0)

            print(num_child, metadata)

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
            print("there")
            print(current_node.key)
            print(current_node.visited)
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

    return tree, asum

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

#region Problem 2
#
#
#
#endregion

### Test cases:

p2_a = ([],0)

p2_test_cases = {
    "p2_a":p2_a
}

### Answers:

def p2answer1(*args, **kwargs):
    pass

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



####### Official Input Data #######

### C"SV library

file_path = "/home/will/advent_of_code/Advent-of-Code/2018/day_08_input.txt"

with open(file_path) as my_file:
    raw_data = my_file.read().split()
    data = []
    for i in raw_data:
        data.append(int(i))

# Data was the same for problem one and two for this day.


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
time_with_official_data(problem_number=2, answer_dict=p2answers, loops=1)

