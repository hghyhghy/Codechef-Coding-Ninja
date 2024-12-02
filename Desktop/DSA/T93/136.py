

#check for BST  

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
        
def main(root,mininum=float("-inf"),maximum=float("inf")):
    
    if not  root:
        
        return  True
    
    if not(mininum<root.val<maximum):
        
        return False
    
    return main(root.left,mininum,root.val) and main(root.right,root.val,maximum)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(11)
root.right.right = TreeNode(20)

print(main(root))