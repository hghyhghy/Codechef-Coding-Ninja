
#searching of an element 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def main(root,target):
    
    if not root or not target:
        
        return None
    
    if root.val == target:
        
        return True
    
    if target < root.val:
        
        return main(root.left,target)

    return main(root.right,target)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

target=5

print(main(root,target))
    