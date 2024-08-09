# height of the binary  tree

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def height_of_tree(root):
    
    if not root:
        
        return 0
    
    left_height=height_of_tree(root.left)
    right_height=height_of_tree(root.right)

    
    return max(left_height,right_height) + 1

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(4)

print(height_of_tree(root))

    
    