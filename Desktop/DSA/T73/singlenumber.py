# Problem statement
# You are given an arbitrary array ‘arr’ consisting of N non-negative integers, where every element appears thrice except one. You need to find the element that appears only once.

def single_number(array:list[int])->int:
    
    freq={}
    
    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    for  num,count in freq.items():
        
        if count == 1:
            
            return num
        
    return -1

a=[2,3,1,1,2,4]
print(single_number(a))