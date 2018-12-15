import timeit
from collections import defaultdict

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
#
# Possible problem solving implementations include a linked list, a trie, a binary tree with left child
# right sibling arrangement.
#
# Starting from scratch all over again. Going to work with a simple binary tree and try to modify it after
# I get a feel for it. I'm looking to make a left child - right sibling binary tree...
#
# LC-RS is exactly the same structure as a binary tree it is simply in the nature of construction that
# causes it to be such.....
#
# This:
#
#        a
#      / | \
#     /  |  \
#    b   c   d
#       / \
#      e   f
#
# Can be represented as:
#
#        a
#       /
#      /
#     b---c---d
#        /
#       e---f
#
# May lead to some slow traversal at times.

# Tree LCRS data structure attempt.
def p1answer2(ls, *args, **kwargs):

p1_a = ([2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2],138)

ls = p1_a[0].copy()


class BinaryTree:
    def __init__(self, rootObj, metadata=None, numChildren=None):
        self.key = rootObj
        self.metadata = metadata
        self.numChildren = numChildren
        self.leftChild = None
        self.rightSibling = None
        self.parent = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            self.leftChild.parent = self

        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            t.leftChild.parent = self
            self.leftChild = t

    def insertRight(self, newNode):
        parent = self.parent
        if self.rightSibling== None:
            self.rightSibling = BinaryTree(newNode)
            self.rightSibling.parent = parent

        else:
            t = BinaryTree(newNode)
            t.rightSibling = self.rightSibling
            t.rightSibling.parent = parent
            self.rightSibling = t

    def setNumChildren(self, obj):
        self.numChildren = obj

    def setMetadata(self, obj):
        self.metadata = obj

    def setRootVal(self, obj):
        self.key = obj

    def getLeftChild(self):
        if self.leftChild:
            print("{0}'s left child is {1}".format(self.key, self.leftChild.key))
        else:
            print(self.leftChild)
        return self.leftChild

    def getRightSibling(self):
        if self.rightSibling:
            print("{0}'s right sibling is {1}".format(self.key, self.rightSibling.key))
        else:
            print(self.rightSibling)
        return self.rightSibling

    def getParent(self):
        print("{0}'s parent is {1}".format(self.key, self.parent.key))
        return self.parent

    def getNumChildren(self):
        # print("{0}'s number of children is {1}".format(self.key, self.numChildren))
        return self.numChildren

    def getMetadata(self):
        return self.metadata

    def getRootVal(self):
        return self.key


def build_tree(current_node, ls):

    if not ls:
        return(current_node)

    if current_node.getNumChildren() > 0:
        node_ID = next(node_ID_generator)
        print(node_ID)
        current_node.insertLeft(node_ID)

        # Create right siblings for the left child just created.
        # Range is minus one because we already created the left child for this level.
        for i in range(1, current_node.getNumChildren()):
            node_ID = next(node_ID_generator)
            current_node.getLeftChild().insertRight(node_ID)

        current_node = current_node.getLeftChild()

        number_of_children = ls.pop(0)
        metadata = ls.pop(0)

        current_node.setNumChildren(number_of_children)
        current_node.setMetadata(metadata)

        return build_tree(current_node, ls)

    if current_node.getNumChildren() == 0 and current_node.getRightSibling() != None:
        meta_ls = []
        for i in range(current_node.getMetadata()):
            value = ls.pop(0)
            meta_ls.append(value)

        current_node.setMetadata(meta_ls)

        current_node = current_node.getRightSibling()

        number_of_children = ls.pop(0)
        metadata = ls.pop(0)

        current_node.setNumChildren(number_of_children)
        current_node.setMetadata(metadata)

        return build_tree(current_node, ls)

    if current_node.getNumChildren() == 0 and current_node.getRightSibling() == None:

        if current_node.getParent() == None:

            return current_node

        else:
            current_node = current_node.getParent()

            return build_tree(current_node, ls)


node_ID_generator = (str(i) for i in range(10))
node_ID = next(node_ID_generator)
A_node = BinaryTree(node_ID)

number_of_children = ls.pop(0)
metadata = ls.pop(0)

A_node.setNumChildren(number_of_children)
A_node.setMetadata(metadata)

build_tree(A_node, ls)

A = A_node
B = A_node.getLeftChild()
C = B.getRightSibling()
D = C.getLeftChild()



# Traversal
#
#
# https://docs.python.org/3/whatsnew/2.3.html?highlight=build%20tree
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
#
# def inorder(t):
#     if t:
#         for x in inorder(t.left):
#             yield x
#         yield t.label
#         for x in inorder(t.right):
#             yield x


a = (i for i in range(20))



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

