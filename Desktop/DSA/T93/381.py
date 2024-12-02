#preorder
from T85.preorder import preoder


class TreeNode:

    def __init__(self,val=0,left=None,right=None):

        self.val=val
        self.left=left
        self.right =right


def main(root):

    r=[]

    def helper(root):

        if not root:

            return

        r.append(root.val)
        helper(root.left)
        helper(root.right)

    helper(root)

    return  r


if __name__ == "__main__":
    # Creating a simple binary tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = preoder(root)

    print(*result)