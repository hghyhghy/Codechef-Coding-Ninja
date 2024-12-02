

#longest consecutive substring

def main(array:list[int])->int:

    n=len(array)
    array.sort()

    max_length=1
    count=1
    
    for i in range(n):
        
        if array[i] == array[i-1]+1:
            
            count +=1 
            
        elif array[i] == array[i-1]:
            
            continue
        
        else:
            
            max_length = max(max_length,count)
            count=1
            
    return max_length

arr = [100, 4, 200, 1, 3, 2]
print(main(arr))