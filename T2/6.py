# array arm val if sum of all odd num is odd then arm val = |sum of even no - sum of odd num| else if  if sum of all odd num is even 
# then arm val = |sum of even no + sum of odd num|

def arm_value_array(arr):
    
    odd=0
    even=0
    
    for i in range(len(arr)):
        
        if arr[i] % 2 == 0:
            
            even += arr[i]

        elif arr[i] % 2 != 0:
            
            odd += arr[i] 
            
            
    if odd % 2 != 0:
        
        return abs(even - odd)

    elif odd % 2 == 0:
        
        return abs(even+odd)


a=[1,2,3,4,5]
print(arm_value_array(a))

