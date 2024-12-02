
#longest substring without repeat char

def main(string):
    
    n=len(string)
    max_len=float("-inf")

    for i in range(n):
        
        seen=set()

        for j in  range(i,n):
            
            if string[j] in seen:
                
                break
            
            seen.add(string[j])

            max_len =max(max_len,j-i+1)

    return max_len

a="abcabcbb"
print(main(a))