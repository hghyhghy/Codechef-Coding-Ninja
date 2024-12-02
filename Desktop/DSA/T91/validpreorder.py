# You are given an array 'ARR' of positive integers. Your task is to check whether the array 'ARR' is a valid Preorder Traversal of a Binary Search Tree.

# A binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree whose internal nodes each store a value greater than or equal all the values in the node's left subtree and less than those in its right subtree.

# For Example
# Consider the array ARR = [ 7, 4, 8 ] having 3 elements. 
# This array represents the pre-order traversal of the below tree. 

# Hence, the above array 'ARR' is a valid Preorder Traversal of a Binary Search Tree.

def valid_preorder(array:list[int])->bool:
    
    n=len(array)
    
    if n==0 or n==1:
        
        return True
    
    root=array[0]
    i=1
    
    while i<n and array[i] < root:
        
        i +=1
        
    for j in range(i,n):
        
        if array[i] < root:
            
            return False
        
    
    return True

arr = [7, 4, 8]
print(valid_preorder(arr))