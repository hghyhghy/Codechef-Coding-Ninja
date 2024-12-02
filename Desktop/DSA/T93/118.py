

#smallest element after k removal

def main(array:list[int],k:int)->int:
    
    stack=[]

    for num in array:
        
        while k>0 and stack and stack[-1]>num:
            
            stack.pop()
            k -=1
            
        stack.append(num)

    
    final = stack[:k] if  k else stack
    
    result="".join(final).lstrip("0")

    return result if result else None

print(main("1432219",3))