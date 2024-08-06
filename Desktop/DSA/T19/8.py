# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

def rearrange_even_odds(array):
    
    store1=[]
    store2=[]

    for num in array:
        
        if num % 2  == 0:
            
            store1.append(num)

        else:
            
            store2.append(num)

    return sorted(store1)+ sorted(store2)

nums = [1, 2, 3, 4, 5, 6]
print(rearrange_even_odds(nums))