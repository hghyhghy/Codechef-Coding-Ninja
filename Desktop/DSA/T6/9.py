# /Longest Subarray with given Sum K

def longest_subarray_with_given_sum (array,target):

    n=len(array)
    lenght=0
    
    for i in range(n):
        
        current_sum = 0
        
        for j in range(i,n):
            
            current_sum += array[j]

            if current_sum ==   target:
                
                lenght = max(lenght,j-i+1)

    return lenght

arr = [1, 2, 3, 4, 5, -1, 2, 3]
K = 6

print(longest_subarray_with_given_sum(arr,K))
