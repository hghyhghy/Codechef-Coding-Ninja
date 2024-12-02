# find the triplet with target_sum

def triplet_with_target_sum(array,target):
    
    n=len(array)
    triplet=[]

    for i in range(n):
        
        for j in range(i+1,n):
            
            for k in range(j+1,n):
                
                if array[i]+array[j]+array[k] == target:
                    
                    triplet.append([array[i],array[j],array[k]])
                    
    return triplet

arr = [1, 2, 3, 4, 5, 6, 7]
target = 12

print(triplet_with_target_sum(arr,target))