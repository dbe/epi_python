from test_framework import generic_test


def is_symmetric(tree):
    if(tree is None):
        return True
        
    return subtree(tree.left, tree.right)

def subtree(a, b):
    a_data = a.data if a else None
    b_data = b.data if b else None

    #Short Circuit
    if(a_data != b_data):
        return False

    #Base Case
    if(a_data is None and b_data is None):
        return True

    return all([subtree(a.right, b.left), subtree(a.left, b.right)])




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
