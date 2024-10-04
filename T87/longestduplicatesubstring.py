# You are given a string 'S' and you need to return the length of the longest duplicate substring in the given string. The occurrence of duplicate sub-strings can overlap also.

# If there are many longest duplicate sub-string return any of them.

def longest_duplicate_substring(string:set)->str:
    n = len(string)
    longest_length = 0  # Variable to store the length of the longest duplicate substring

    # Iterate over all possible start points of the substrings
    for start in range(n):
        # Iterate over all possible end points of the substrings
        for end in range(start,n):  # end is exclusive
            substring = string[start:end]
            
            # Check if the substring appears more than once in the string
            if string.count(substring) > 1:
                # Update longest_length if this substring is longer than the current longest
                longest_length = max(longest_length, len(substring))

    return longest_length
    return longest 

S = "banana"
print(longest_duplicate_substring(S))
            
            