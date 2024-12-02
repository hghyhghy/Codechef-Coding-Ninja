

#valid preorder 

def main(array):
    
    stack=[]
    root=float("-inf")

    for num in array:
        
        if num<root:
            
            return False
        
        while stack and stack[-1]<num:
            
            stack.pop()

        stack.append(num)

    return True

ARR = [40, 30, 35, 80, 100]
print(main(ARR))