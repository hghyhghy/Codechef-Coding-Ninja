

#bubble sort 

def main(array):
    
    n=len(array)

    for i in range(n):
        
        for j in range(0,n-i-1):
            
            if array[j]>array[j+1]:
                
                array[j],array[j+1]=array[j+1],array[j]
                
    return array

nums=list(map(int,input().split()))
print(main(nums))