# Problem statement
# You are given with an array of integers and an integer K. You have to find and print the count of all such pairs which have difference K.

# Note: Take absolute difference between the elements of the array.

def pair_with_difference_k(array,diff):
    
    store=[]
    n=len(array)
    count =0 
    if not array or n==1:
        
        return 
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if abs(array[i] - array[j]) ==  diff:
                
                store.append([array[i],array[j]])
                count+= 1

    return store,count

arr = [1, 5, 3, 4, 2]
K = 2
print(pair_with_difference_k(arr,K))

