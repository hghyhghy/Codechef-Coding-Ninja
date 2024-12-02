# Problem statement
# You are given a string S of words. Your task is to count the occurrence of each word present in the string S. A word is a sequence of one or more non-space characters, and there can be multiple spaces between two words, and also there can be leading or trailing spaces in a string S.

def occurance_of_word(words):
    
    words=words.split()

    count={}
    for word in words:
        if word in count:
            
           count[word] += 1
           
        else:
            count[word] = 1
            
    return count

a="what we think we become"
print(occurance_of_word(a))