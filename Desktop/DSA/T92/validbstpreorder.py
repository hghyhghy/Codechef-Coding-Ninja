# Problem statement
# You are given an array/list ‘ARR’ consisting of ‘N’ distinct integers. You need to check whether ‘ARR’ can represent the Preorder Traversal of a Binary Search Tree.

# You should return true if ‘ARR’ can represent Preorder Traversal of a Binary Search Tree, otherwise return false.

def can_validate_bst_preorder(array:list[int])->bool:
    
    stack=[]
    root=float("-inf")

    for num in array:
        
        if num< root:
            
            return False
        
        while stack and stack[-1] < num:
            
            root=stack.pop()

        
        stack.append(num)
        
    
    return True

ARR = [40, 30, 35, 80, 100]
print(can_validate_bst_preorder(ARR))