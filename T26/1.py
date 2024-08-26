# Write a program to find a word in a given string which has the highest number of repeated letters

def count_max_chars(string):
    
    freq={}

    for chr in string:
        
        if chr in freq:
            
            freq[chr] += 1
            
        else:
            
            freq[chr] = 1
            
            
    max_repeats=max(freq.values())

    return max_repeats

def max_repeated_letters(s):
    
    words=s.split()
    max_repeated= 0
    max_word=""
    for  word in words:
        
        if count_max_chars(word) > max_repeated:
            
            max_repeated = count_max_chars(word)
            max_word = word
            
    
    return max_word

input_string = "apple banana grape orange"
print(max_repeated_letters(input_string))