from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> List[int]:
    """Traverses a tree given with root in the in-order manner.

    Args:
        root (TreeNode): Root of the tree.

    Returns:
        List[int]: List of node values.
    """
    
    list_values = []
    
    if root is not None:
        # Left visit
        return_left = inorderTraversal(root.left)
        return_left.append(root.val)

        # Visiting the root
        list_values.extend(return_left)

        # Right visit
        return_right = inorderTraversal(root.right)
        list_values.extend(return_right)

        return list_values
    else:
        return []


def main():
    tree = TreeNode(0, TreeNode(1,TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(6)))))
    ans = inorderTraversal(tree)
    
    print(ans)
    
    
if __name__ == '__main__':
    main()
    