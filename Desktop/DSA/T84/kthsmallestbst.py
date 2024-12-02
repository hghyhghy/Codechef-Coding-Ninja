# Problem statement
# Given a binary search tree and an integer ‘K’. Your task is to find the ‘K-th’ smallest element in the given BST( binary search tree).

# BST ( binary search tree) -

# If all the smallest nodes on the left side and all the greater nodes on the right side of the node current node.

class BinaryTreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def inorder(root,element):
    
    if root:
        
        inorder(root.left,element)
        
        element.append(root.val)

        inorder(root.right,element)


def kth_smallest(root,k):
    
    element=[]
    
    inorder(root,element)

    if 0<k<=len(element):
        
        return element[k-1]
    
    else:
        
        return  None
    
    
root = BinaryTreeNode(5)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(7)
root.left.left = BinaryTreeNode(2)
root.left.right = BinaryTreeNode(4)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(8)

# Finding the 3rd smallest element
K = 3
result = kth_smallest(root, K)
if result is not None:
    print(f"The {K}-th smallest element in the BST is: {result}")
else:
    print(f"The {K}-th smallest element does not exist.")