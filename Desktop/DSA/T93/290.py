


#lds 

def main(array):
    
    stack=[]
    for num in array:
        
        if not stack and stack[-1] > num:
            
            stack.append(num)

        else:
            
            for i in range(len(stack)):
                
                if stack[i] <= num:
                    
                    stack[i] = num
                    
    return stack,len(stack)
    
        