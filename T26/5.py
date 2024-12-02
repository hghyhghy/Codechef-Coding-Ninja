# You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'.

# Note:

# Each pair should be sorted i.e the first value should be less than or equals to the second value. 

# Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.

def finding_pairs(arr,s):
    
    pairs=[]

    n=len(arr)

    for i in range(n):
        
        for j in range(i+1,n):
            
            if arr[i] + arr[j] == s:
                
                if arr[i] <= arr[j]:
                    
                    pairs.append((arr[i],arr[j]))

                else:
                    
                    pairs.append((arr[j],arr[i]))


    pairs=sorted(set(pairs))

    return pairs


arr = [1, 3, 2, 2, 4, 0, 5, 3]
S = 5

print(finding_pairs(arr,S))