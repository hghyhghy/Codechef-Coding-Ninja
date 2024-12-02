#longest decreasing subsequence 

def main(array:list[int])->int:
    
    if not array:
        return 0
    
    stack=[]

    for num in array:
        
        if not stack or stack[-1]>num:
            
            stack.append(num)
            
        else:
            
            for i in range(len(stack)):
                
                if stack[i]<=num:
                    
                    stack[i]=num
                    break
    
    return len(stack)

arr = [5, 0, 3, 2, 9]
print(main(arr))