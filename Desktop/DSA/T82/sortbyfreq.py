# Problem statement
# You are given a list of a repeated set of integers. Your task for the problem is to return a list of the given elements in decreasing sorted order of their frequency of repetition in the given list with the element with the highest frequency of repetition first and so on.

# Note :
# If two numbers have the same frequency then keep the one that was present before the other in the original given list (array) first.
# For Example :
# Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
# Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

# Explanation :
# When you sort the array based on the decreasing order of the frequency of repetition of integers in the original array, 
# you’ll find that the element ‘8’ is the integer with the most repeated values therefore it would be arranged first after which since both 2 and 5 have the same number of repeated 
# values in the original array but since the 2 arrived first so we will first arrange 2 and then 5 in our resultant array, while would be the last element after sorting here.


def sort_array_by_frequency(array:list[int])->list[int]:
    
        freq={}
        first={}
        
        for index,num in enumerate(array):
            
            if num in freq:
                
                freq[num] += 1
                
            else:
                
                freq[num]=1
                first[num] = index
                
                
        new_array =sorted(array,key=lambda x: (-freq[x],first[x]))
        
        return new_array
    

arr = [2, 5, 2, 8, 5, 6, 8, 8]
print(sort_array_by_frequency(arr))