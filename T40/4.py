# Problem statement
# You have been given a Binary Tree of integers, find the minimum depth of this Binary Tree. The minimum depth of a Binary Tree is the number of nodes along the shortest path from the root node down to the nearest leaf node.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def height_of_BST(root):
    
    if root is None:
        
        return 0
    
    left=height_of_BST(root.left)
    right=height_of_BST(root.right)

    return max(left,right)+ 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(height_of_BST(root))