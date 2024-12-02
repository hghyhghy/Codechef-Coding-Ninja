# You are given a string ‘S’ of length ‘N’. You have to return all the characters in the string that are duplicated and their frequency. bys uisng dict You are given a string ‘S’ of length ‘N’. You have to return all the characters in the string that are duplicated and their frequency. bys uisng dict 

def most_freq_char_and_frequency(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] += 1
            
        else:
            
            freq[char] = 1
            
    result={char:count  for char,count in freq.items() if count > 1}
    
    return result

S = "programming"
print(most_freq_char_and_frequency(S))