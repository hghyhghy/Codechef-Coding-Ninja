# Problem statement
# There is a Binary Search Tree (BST) consisting of ‘N’ nodes. Each node of this BST has some integer data.



# You are given the root node of this BST, and an integer ‘X’. Return true if there is a node in BST having data equal to ‘X’, otherwise return false.



# A binary search tree (BST) is a binary tree data structure that has the following properties:

# 1. The left subtree of a node contains only nodes with data less than the node’s data.

# 2. The right subtree of a node contains only nodes with data greater than the node’s data.

# 3. The left and right subtrees must also be binary search trees.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def finding_element_in_the_BST(root,target):
    
    if root is None:
        
        return False
    
    if root.val ==  target:
        
        return True
    
    if target < root.val:
        
        return finding_element_in_the_BST(root.left,target)

    
    return finding_element_in_the_BST(root.right,target)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

target=5

print(finding_element_in_the_BST(root,target))