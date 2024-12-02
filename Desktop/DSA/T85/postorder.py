# Problem statement
# You have been given a Binary Tree of 'n' nodes, where the nodes have integer values. Your task is to return its postorder traversal.



# For Example:
# For the given tree below,
# Postorder traversal for the given tree will be [4, 5, 2, 3, 1]. Hence, the answer is [4, 5, 2, 3, 1].

class TreeNode:
    
    def  __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
        
def postorder(root):
    
    result=[]
    
    def helper(root):
        
        if not root:
            
            return 
        
        helper(root.left)

        helper(root.right)

        result.append(root.val)

    
    helper(root)

    return result

if __name__ == "__main__":
    # Example tree: 
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    # Get the postorder traversal
    result = postorder(root)
    
    # Print the result
    print(*result)