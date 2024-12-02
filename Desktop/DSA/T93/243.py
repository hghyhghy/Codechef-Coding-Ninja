
#longest consecutive array

def main(array:list[int])->list[int]:
    
    array.sort()
    array=list(set(array))
    longest=float("-inf")
    n=len(array)


    for i in range(n):
        
        current = 1
        
        for j in range(i+1,n):
            
            if array[j] == array[j-1]+1:
                
                current +=1
                
            else:
                
                break
            
        longest=max(longest,current)

    
    return longest

arr = [100, 4, 200, 1, 3, 2]
print(main(arr))
    
    