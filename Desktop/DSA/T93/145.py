

#maximum common element sum 

def main(arr1,arr2):
    
    common =  list(set(arr1)&set(arr2))
    if len(common) < 2:
        
        return
    
    max_sum=float("-inf")
    pair=None
    n=len(common)
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            current=  common[i] + common[j]

            if current > max_sum:
                
                max_sum =  current
                pair=(common[i],common[j])

     
        return max_sum,pair
    
    return common

arr1 = [1, 5, 3, 8, 12]
arr2 = [3, 8, 7, 10, 5]
print(main(arr1,arr2))