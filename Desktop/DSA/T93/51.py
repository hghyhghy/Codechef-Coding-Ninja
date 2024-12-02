
#count pairs with zero 

def main(array:list[int])->int:
    
    n=len(array)
    count = 0
    
    for i  in range(n):
        
        for j in range(i+1,n):
            
            if array[i] + array[j]== 0:
                
                count += 1
                
    return count

n=list(map(int,input().split()))
print(main(n))