
# ou are given a function,

# Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

# The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

# Assumption: String Contains only lower-case alphabetical letters.

def replacing_char(string,c1,c2):

    if not string:

        return None
    
    char_List= list(string)
    for i in range(len(char_List)):

        if char_List[i]==  c1:

            char_List[i] = c2

        elif char_List[i] == c2:

            char_List[i]=c1

    modified ="".join(char_List)

    
    return modified

Str= "apples"
ch1="a"
ch2="p"

print(replacing_char(Str,ch1,ch2))