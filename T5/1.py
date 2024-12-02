# Write a program to find the largest word in a given string

def largest_word(s):
    
    words = s.split()

    max_word=""

    for word in words:
        
        if len(word) > len(max_word):
            
            max_word = word
            
            
    return max_word

s = "Find the largest word in this sentence"
print(largest_word(s))

    