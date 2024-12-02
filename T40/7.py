# Problem statement
# Given a binary search tree and an integer ‘K’. Your task is to find the ‘K-th’ smallest element in the given BST( binary search tree).

# BST ( binary search tree) -

# If all the smallest nodes on the left side and all the greater nodes on the right side of the node current node.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def smallest_element_from_BST(root):
    
    if root is None:
        
        return None
    
    current=root
    while current.left:
        
        current=current.left
        
    return current.val

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

print(smallest_element_from_BST(root))