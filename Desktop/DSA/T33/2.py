# largets element in the binary search tree 

class TreeNode:
    
    def __init__(tree,val=0,left=None,right=None):
        
        tree.val=val
        tree.left=left
        tree.right=right


def largest_element_from_BST(root):
    
    if not root:
        
        return None
    
    current=root
    
    while current and current.right:
        
        current=current.right
        
    return current.val if current else None

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

print(largest_element_from_BST(root))
    
    