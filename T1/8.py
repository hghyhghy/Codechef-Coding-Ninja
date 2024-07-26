# The function accepts two strings ‘str1’ and ‘str2’ as its argument. The function needs to return the index of the first occurrence of substring ‘str2’ in string ‘str1’ or -1 if the substring is not found.

def finding_string(s1,s2):
    
    words=s1.split()

    for  i in range(len(words)):
        
        if words[i] ==  s2:
            
            return i
        
        
a1="hello world"
a2="world"

print(finding_string(a1,a2))