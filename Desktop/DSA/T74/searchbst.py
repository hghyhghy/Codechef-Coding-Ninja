# Problem statement
# There is a Binary Search Tree (BST) consisting of ‘N’ nodes. Each node of this BST has some integer data.



# You are given the root node of this BST, and an integer ‘X’. Return true if there is a node in BST having data equal to ‘X’, otherwise return false.



# A binary search tree (BST) is a binary tree data structure that has the following properties:

# 1. The left subtree of a node contains only nodes with data less than the node’s data.

# 2. The right subtree of a node contains only nodes with data greater than the node’s data.

# 3. The left and right subtrees must also be binary search trees

class Node:

    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        

def search_bst(root,target):
    
    if not root or not target:
        
        return False
    
    if root.val == target:
        
        return True
    
    if target<root.val:
        
        return search_bst(root.left,target)
    
        
    return search_bst(root.right,target)

if __name__ == "__main__":
    # Create the BST manually
    # Example tree:
    #        50
    #       /  \
    #      30   70
    #     / \   / \
    #    20 40 60 80
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    # Search for the value 'X' in the BST
    X = 60
    result = search_bst(root, X)
    print(f"Is {X} present in the BST? {'Yes' if result else 'No'}")

    # Search for another value
    X = 100
    result = search_bst(root, X)
    print(f"Is {X} present in the BST? {'Yes' if result else 'No'}")
    
    