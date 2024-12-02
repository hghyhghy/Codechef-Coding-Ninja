

# triplet sum less than k 

def  main(array,target):
    
    n=len(array)
    array.sort()

    count = 0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if array[i]+array[j]+array[k] < target:
                    
                    count += 1
                    
    return count

target=2
nums=list(map(int,input().split()))

print(main(nums,target))
