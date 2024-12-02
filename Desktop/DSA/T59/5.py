# You are given a string STR of length N consisting of lowercase English Alphabet letters. Your task is to return the count of minimum characters to be added at front to make the string a palindrome.

def minimum_character_to_add(string):

    reversed_string=string[::-1]

    n=len(string)

    for i in range(n):
        
        if string[i:]==reversed_string[:n-i]:
            
            return i
        
    return None

STR1 = "abcd"
print(minimum_character_to_add(STR1))
    
