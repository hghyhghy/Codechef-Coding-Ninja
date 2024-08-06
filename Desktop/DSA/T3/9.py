# Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

# Note: All pairs should be printed in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then
# (u1,v1) should be printed first else second.


def finding_matching_pair(a,b,target):
    
    a.sort()
    b.sort()

    i=0
    j=len(b)-1
    
    pairs=[]
    while i < len(a) and j>=0:
        
        current_sum = a[i] + b[j]

        if current_sum ==  target:
            
            pairs.append([a[i],b[j]])
            i += 1
            j -= 1
            
        elif current_sum < target:
            
            i += 1
            
        else:
            
            j -= 1
            
    return pairs

A = [1, 2, 4, 5, 7]
B = [5, 6, 3, 4, 8]
X = 9
         
print(finding_matching_pair(A,B,X))