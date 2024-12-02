# You have been given a sorted array of length ‘N’. You need to construct a balanced binary search tree from the array. If there can be more than one possible tree, then you can return any.

# Note:

# 1. A balanced binary tree is a binary tree structure in which the left and right subtrees of every node differ in height by no more than 1.

# 2. A binary search tree is a binary tree data structure, with the following properties
#     a. The left subtree of any node contains nodes with value less than the node’s value.
#     b. The right subtree of any node contains nodes with values equal to or greater than the node’s value.
#     c. Right, and left subtrees are also binary search trees.
# Example:

# Below tree, is a balanced binary search tree

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
    
    root.right=construct(array[mid+1:])
    
    return root

def inorder(root):
    
    if not root:
        
        return []
    
    return inorder(root.left)+[root.val]+inorder(root.right)

sorted_array = [-10, -3, 0, 5, 9]
bst_root = construct(sorted_array)

# Now perform in-order traversal to verify the tree structure
print(inorder(bst_root)) 