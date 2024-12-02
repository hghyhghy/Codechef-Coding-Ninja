

#max coonsecutive one 

def main(array:list[int])->int:
    
    n=len(array)
    max_count=float("-inf")
    count=0
    
    for i in range(n):
        
        if array[i] == 1:
            
            count +=1
            
        else:
            
            max_count=max(max_count,count)
            count =0
            
            
    max_count=max(max_count,count)

    return max_count

arr=list(map(int,input().split()))
print(main(arr))