import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(a, b):
    height_a = height(a)
    height_b = height(b)
    diff = abs(height_a - height_b)

    if(height_a < height_b):
        for _ in range(diff):
            b = b.parent
    elif(height_b < height_a):
        for _ in range(diff):
            a = a.parent

    
    while(True):
        #Will never run into a problem of running out of nodes because the root will always at least be the LCA
        if(a == b):
            return a
        a = a.parent
        b = b.parent

#O(n)
def height(a):
    height = 1

    while(a.parent is not None):
        a = a.parent
        height += 1

    return height



@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
