
#height of the tree 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def main(root):
    
    if not root:
        
        return 0
    
    left=main(root.left)
    right=main(root.right)

    return 1+max(left,right)

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

    print("Height of the tree:", main(root)) 