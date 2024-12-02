
# Given an array/list 'ARR' of integers and an integer ‘K’. You are supposed to return the length of the shortest subarray that has a sum greater than or equal to ‘K’. If there is no subarray with a sum greater than or equal to K, then return -1.

# Note :
# An array ‘B’ is a subarray of an array ‘A’ if ‘B’ that can be obtained by deletion of, several elements(possibly none) from the start of ‘A’ and several elements(possibly none) from the end of ‘A’. 


def shortest_subarray_with_sum_atleast_k(array:list[int],k:int)->int:
    
    n=len(array)
    max_len=float("inf")

    for i in range(n):
        
        current= 0
        
        for j in range(i,n):
            
            current += array[j]

            if current >=k:
                
                max_len =  min(max_len ,j-i+1)
                
                break
            
    return max_len if max_len!= float("-inf") else -1

a=int(input("enter"))
arr1=list(map(int,input().split()))

print(shortest_subarray_with_sum_atleast_k(arr1,a))