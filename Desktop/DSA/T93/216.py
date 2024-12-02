

#maximum freq element

def main(string):
    
    freq={}

    for char in string:
        
        if char in freq:
            
            freq[char] +=1
            
        else:
            
            freq[char] =1
            
    character=[char for char,count in freq.items() if count > 1]

    return character

n=[ 1, 2, 3, 1, 2]
print(main(n))