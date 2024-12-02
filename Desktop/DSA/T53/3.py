# Problem statement
# You are given a string 'S' of length 'N', you need to find the frequency of each of the characters from ‘a’ to ‘z’ in the given string.

# Example :

def count_frequency(array):
    
    freq={}

    for num in array:
        
        if num in freq:
            
            freq[num] += 1
            
        else:
            
            freq[num] = 1
            
    return freq

a="abcdg"
print(count_frequency(a))