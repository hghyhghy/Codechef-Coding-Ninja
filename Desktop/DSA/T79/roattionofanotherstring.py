# Problem statement
# You are given two Strings 'P' and 'Q' of equal length.



# Your task is to return 1 if String 'P' can be converted into String 'Q' by cyclically rotating it to the right any number of times ( Possibly Zero ), else return 0.



# A cyclic rotation to the right on String 'A' consists of taking String 'A' and moving the rightmost character to the leftmost position. For example, if 'A' = "pqrst", then it will be "tpqrs" after one cyclic rotation on 'A'.

def check_if_rotated_or_not(p:str,q:str)->int:
    
    if len(p)  != len(q):
        
        return 0
    
    for _ in range(len(p)):
        
        if p == q:
            
            return 1
        
        p=p[-1]+p[:-1]
        
        
    return 0

P = "pqrst"
Q = "tpqrs"
print(check_if_rotated_or_not(P,Q))