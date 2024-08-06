# Given a string s and an integer k, reverse the first k character

def reverse_kth_elements(string,k):
    
    reversed_version= string[:k][::-1]
    remained_part= string[k:]

    
    return reversed_version+remained_part

s = "abcdefgh"
k = 4

print(reverse_kth_elements(s,k))
