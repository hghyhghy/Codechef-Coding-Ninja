#kth largest element in the bst 

class BinaryTreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def reverse_inorder(root,ele):
    
    if root:
        
        reverse_inorder(root.right,ele)
        
        ele.append(root.val)

        reverse_inorder(root.left,ele)
        

def kth_largest(root,k):
    
    element= []

    reverse_inorder(root,element)

    if 0<k<=len(element):
        
        return element[k-1]
    
    else:
        
        return None
    
root = BinaryTreeNode(5)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(2)
root.left.right = BinaryTreeNode(4)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(8)

# Finding the 3rd largest element
K = 3
result = kth_largest(root, K)
if result is not None:
    print(f"The {K}-th largest element in the BST is: {result}")
else:
    print(f"The {K}-th largest element does not exist.")