# Problem statement
# You are given with an array of integers and an integer K. You have to find and print the count of all such pairs which have difference K.

# Note: Take absolute difference between the elements of the array.

def finding_pair_with_given_sum(array:list[int],k:int)->int:

    n=len(array)
    count= 0
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if array[j] - array[i] == k:
                
                count += 1
                
    return count

arr = [1, 5, 2, 1, 3, 4, 2]
K = 2
print(finding_pair_with_given_sum(arr,K))
    
    