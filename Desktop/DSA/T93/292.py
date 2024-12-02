
#postorder

class ListNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
        
def postorder(root):
    
    if root:
        
        postorder(root.left)

        postorder(root.right)

        print(root.val)

