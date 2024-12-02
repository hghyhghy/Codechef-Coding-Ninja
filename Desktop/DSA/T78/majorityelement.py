# Problem statement
# You are given an array ‘ARR’ and another integer number ‘K’. Your task is to find the all elements of ‘ARR’ which occur more than or equals to ‘N/K’ times in ‘ARR’ and ‘N’ is the length of array ‘ARR’.

# For example:

# Given array ‘ARR = { 1, 2, 3, 3, 3, 3, 4, 4, 4, 1, 2 ,0}’ and ‘K = 4’
# Answer is {3, 4} because ‘3’ occurs ‘4’ times and ‘4’ occurs ‘3’ times which is more than or equals to ‘12/ 4 =3’.


def majority_element(array:list[int],k:int)->list[int]:
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] +=1
            
        else:
            
            freq[num]=1
            
    n=len(array)
    limit = n//k
    result=[]
    
    
    for num,count in freq.items():
        
        if count >= limit:
            
            result.append(num)
            
    return result  

arr = [1, 2, 3, 3, 3, 3, 4, 4, 4, 1, 2, 0]
n = len(arr)
k = 4
print(majority_element(arr,k))