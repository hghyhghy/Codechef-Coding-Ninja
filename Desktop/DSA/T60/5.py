# Problem statement
# You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

# Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

# For Example :
# If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.

def subsets_equals_to_k(array,k):
    
    possble={0}

    for num in array:
        
        seen=set()

        for value in possble:
            
            total =  value+num
            seen.add(total)

            if total == k:
                
                return True
            
        possble.update(seen)

    return k in possble 

ARR = [1, 2, 3, 7]
K = 15

print(subsets_equals_to_k(ARR,K))