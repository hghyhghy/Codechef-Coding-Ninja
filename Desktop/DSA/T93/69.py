
#array to bst 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def construct(array):
    
    if not array:
        
        return None
    
    mid=len(array)//2

    root=TreeNode(array[mid])

    root.left=construct(array[:mid])

    root.right =  construct(array[mid+1:])

    return root

def inorder(root):
    
    if not root:
        return []
    
    return inorder(root.left)+[root.val]+inorder(root.right)

sorted_array = list(map(int,input().split()))
bst_root = construct(sorted_array)

# Now perform in-order traversal to verify the tree structure
print(inorder(bst_root)) 
    
    