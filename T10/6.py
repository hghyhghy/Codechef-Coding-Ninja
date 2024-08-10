# kth smallest element in BST 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
        
def collection(root):
    
    elements=[]

    def inorder_traversal(root):
        
        if root is None:
            
            return 
        
        inorder_traversal(root.left)
        elements.append(root.val)
        inorder_traversal(root.right)

    
    inorder_traversal(root)
    return elements

def kth_smallest_element(root,k):
    
    element=collection(root)
    element.sort()
    return element[k-1]

root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
k = 3
print(kth_smallest_element(root,k))

