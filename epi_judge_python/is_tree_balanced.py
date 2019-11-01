from test_framework import generic_test

def is_balanced_binary_tree(tree):
    if(not tree):
        return True

    balanced, height = traverse(tree, 1)

    return balanced

def traverse(node, level):
    left = right = level

    if(node.left):
        balanced, left = traverse(node.left, level + 1)
        if(not balanced):
            return (False, -1)

    if(node.right):
        balanced, right = traverse(node.right, level + 1)
        if(not balanced):
            return (False, -1)

    balanced = abs(right - left) < 2
    height = max(left, right)


    return (balanced, height)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
