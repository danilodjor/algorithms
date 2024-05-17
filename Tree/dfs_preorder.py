from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode) -> List[int]:
    """Traverses a tree given with root in the pre-order manner.

    Args:
        root (TreeNode): Root of the tree.

    Returns:
        List[int]: List of node values.
    """
    
    output = []
    if root:
        output.append(root.val)
        output += preorderTraversal(root.left)
        output += preorderTraversal(root.right)

    return output


def main():
    tree = TreeNode(0, TreeNode(1,TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(6)))))
    ans = preorderTraversal(tree)
    
    print(ans)
    
    
if __name__ == '__main__':
    main()
    