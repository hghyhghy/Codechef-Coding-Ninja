# most common word in the string 

import re 

def most_common_word(paragraph,banned):
    
    paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()

    words=paragraph.split()

    banned_set=set(banned)

    words_count={}

    for word in words:
        
        if word not in banned_set:
            
            if word in words_count:
                
                words_count[word] += 1
                
            else:
                
                words_count[word] = 1
                
                
    count=0
    string=""

    for char,freq in words_count.items():
        
        if freq > count:
            
            count = freq
            string=char
            
    return string

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(most_common_word(paragraph,banned))
