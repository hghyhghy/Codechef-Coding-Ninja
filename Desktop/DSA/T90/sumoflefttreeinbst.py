# Problem statement
# Given a binary tree with ‘root’. Your task is to find the sum of all the left leaf nodes.

# Properties of leaf:-

# In a binary tree, a leaf is a node such that it does not have any children. Node ‘1’ is always the root of the binary tree. Left leaves are those nodes that are the left child of their parent and a leaf node.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def is_leaf(node):
    
    return node is not None and node.left is None and node.right is None

def sum_of_left(root):
    
    if root is None:
        
        return 0
    
    net_sum = 0

    if root.left and is_leaf(root.left):
        
        net_sum += root.left.val
        
    
    net_sum += sum_of_left(root.left)
    net_sum += sum_of_left(root.right)

    return net_sum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(sum_of_left(root))
        
        
