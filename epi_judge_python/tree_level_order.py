from test_framework import generic_test
from queue import Queue


def binary_tree_depth_order(tree):
    a = Queue()
    b = Queue()
    a.put(tree)
    out = []

    while(not a.empty() or not b.empty()):
        group = []
        while(not a.empty()):
            node = a.get()
            if(node is None):
                continue

            b.put(node.left)
            b.put(node.right)
            group.append(node.data)

        if(len(group) > 0):
            out.append(group)
        group = []
        while(not b.empty()):
            node = b.get()
            if(node is None):
                continue

            a.put(node.left)
            a.put(node.right)
            group.append(node.data)

        if(len(group) > 0):
            out.append(group)

    return out




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
