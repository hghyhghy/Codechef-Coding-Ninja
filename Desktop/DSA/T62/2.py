# Problem statement
# You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

# Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

# For Example :
# If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.

def find_possible_pairs(array,target):
    
    possible={0}

    for num in array:
        
        seen=set()

        for s in possible:
            
            total= s+num
            
            if total == target:
                
                return True
            
            seen.add(total)

        possible.update(seen)

arr = [1, 2, 3, 4, 5]
k = 9

print(find_possible_pairs(arr,k))