# Your friends gifted you a lot of things on your birthday, and now it's your turn to give some return gifts to them. You went to a gift store and decided to buy some Binary Search Trees (BST).

# There is no salesperson in the store. So you are supposed to guess the price of a given BST, which is the minimum value in its nodes.

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right

def minimum_in_bst(root):
    
    if root is None:
        
        return
    
    current=root
    
    while current.left is not None:
        
        current=current.left
        
    return current.val

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)

print(minimum_in_bst(root))