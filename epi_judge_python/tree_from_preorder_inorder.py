from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder, inorder):
    print(f"preorder: {preorder}")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
