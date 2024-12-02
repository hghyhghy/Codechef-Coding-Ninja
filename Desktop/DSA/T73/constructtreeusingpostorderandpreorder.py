
# Problem statement
# You are given a preorder traversal of a binary search tree. Your task is to find the postorder from the preorder.



# Return the root of the BST constructed from the given preorder. The driver code will then use this root to print the post-order traversal.



# For example:
# You are given preOrder = [10, 5, 1, 7, 40, 50], the binary search tree from the given preorder traversal is 

class TreeNode:
    
    def __init__(self,val=0,left=None,right=None):
        
        self.val=val
        self.left=left
        self.right=right
        
def construct(preorder):
    
    if not preorder:
        
        return None
    
    root=TreeNode(preorder[0])

    left1=[x for x in preorder if x<root.val]
    right1=[x for x in preorder if x>root.val]

    root.left=construct(left1)
    root.right=construct(right1)

    return root


def postorder(root):
    
    if not root:
        
        return []

    return postorder(root.left)+postorder(root.right)+[root.val]


def main(preorder):
    
    root=construct(preorder)

    postoder_travresal= postorder(root)

    return postoder_travresal

preorder = [10, 5, 1, 7, 40, 50]
print(main(preorder))
    
    