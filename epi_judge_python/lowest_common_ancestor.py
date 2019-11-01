import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(root, a, b):
    (found_a, found_b, answer) = foo(root, a, b)
    return answer

def foo(node, a, b):
    found_a = found_b = False

    if(node.left):
        ret_a, ret_b, answer = foo(node.left, a, b)
        if(answer):
            return (None, None, answer)
        found_a = found_a or ret_a
        found_b = found_b or ret_b
    if(node.right):
        ret_a, ret_b, answer = foo(node.right, a, b)
        if(answer):
            return (None, None, answer)
        found_a = found_a or ret_a
        found_b = found_b or ret_b

    found_a = found_a or node == a
    found_b = found_b or node == b

    if(found_a and found_b):
        return (None, None, node)
    else:
        return (found_a, found_b, None)



@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
