# Problem statement
# The height of a tree is equal to the number of nodes on the longest path from the root to a leaf.



# You are given an arbitrary binary tree consisting of 'n' nodes where each node is associated with a certain value.



# Find out the height of the tree.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def height_of_tree(root):
    
    if not root:
        
        return 0
    
    left=height_of_tree(root.left)

    right=height_of_tree(root.right)

    return 1+ max(left,right)

if __name__ == "__main__":
    # Creating a simple binary tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Height of the tree:", height_of_tree(root)) 