# Problem statement
# Alice and Bob were given homework to bring a number. As usual, Bob forgot to do it and asked Alice if he could copy her’s. Alice agreed to help him only if he rearranged the digits of her number such that the new number was strictly greater than the old one. Also, the teacher does not like big numbers, so Bob needs to make sure his number is as small as possible.

# Help Bob rearrange the digits of Alice’s number to make a number greater than that of Alice and is smallest possible or print -1 when no such number exists

from itertools import permutations

def next_greater_element(num:int)->int:
    
    num_str=str(num)

    see=set()
    
    for perm in permutations(num_str):
        
        perm_num = int("".join(perm))
        
        if perm_num > num:
            
            see.add(perm_num)

    
    if see:
        
        return min(see)
    
    else:
        
        return -1
    
alice_number = 218765
print(next_greater_element(alice_number))