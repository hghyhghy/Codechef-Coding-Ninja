# You have been given a Binary Tree of 'N' nodes, where the nodes have integer values. Your task is to find the Pre-Order traversal of the given binary tree.

# For example :
# For the given binary tree:

# The Preorder traversal will be [1, 3, 5, 2, 4, 7, 6].
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 0 <= N <= 3000
# 0 <= data <= 10^9     

# Where 'data' denotes the node value of the binary tree nodes.

# Time limit: 1 sec
# Sample Input 1 :
# 2
# 1 2 3 -1 -1 -1  6 -1 -1
# 1 2 3 -1 -1 -1 -1
# Sample Output 1 :
# 1 2 3 6
# 1 2 3
# Explanation of Sample Output 1 :
#  In test case 1, the given binary tree is shown below:

# Preorder traversal of given tree = [1, 2, 3, 6]

# In test case 2, the given binary tree is shown below:

# Preorder traversal of given tree = [1, 2, 3]
# Sample Input 2 :
# 2
# 1 -1 -1
# 1 2 4 5 3 -1 -1 -1 -1 -1 -1
# Sample Output 2 :
# 1
# 1 2 5 3 4
# Explanation of Sample Output 2 :
# In test case 1, there is only one node, so Pre-Order traversal will be only [1].

# In test case 2, the given binary tree is shown below:

# Preorder traversal of given tree = [1, 2, 5, 3, 4]

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def preoder(root):
    
    result=[]

    def helper(root):
        
        if root:
            
            result.append(root.val)

            helper(root.left)

            helper(root.right)

    helper(root)
    
    return result

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
    
    result=preoder(root)
    
    print(*result)