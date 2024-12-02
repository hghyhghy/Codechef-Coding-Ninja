

#longest subarray without repeating char 

def main(array):
    
    n=len(array)
    max_len=float("-inf")

    for i in range(n):
        
        seen=set()

        for j in range(i,n):
            
            if array[j] in seen:
                
                break
            
            seen.add(array[j])

            length= j-i+1
            
            max_len =max(max_len,length)

    return max_len

s = "abcabcbb"
print(main(s))