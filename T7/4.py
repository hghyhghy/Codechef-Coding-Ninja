# Two Sum : Check if a pair with given sum exists in Array

def two_pair_sum(array,target):
    
    n=len(array)

    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[i] + array[j]== target:
                
                return True
            
    
    return False

arr = [1, 2, 3, 4, 5]
target = 9
print(two_pair_sum(arr,target))