# Problem statement
# You have been given the Inorder Traversal and Level Order Traversal of a Binary Tree of integers. Your task is to calculate the height of the Binary tree without constructing it.

# The height of the binary tree is the number of edges in the longest path from the root node to any leaf node in the tree. In case the tree has only one node, the height is taken to be 0


class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def height_of_the_binary_tree(root):
    
    if root is None:
        
        return 0
    
    left=height_of_the_binary_tree(root.left)
    right=height_of_the_binary_tree(root.right)

    return max(left,right) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(height_of_the_binary_tree(root))