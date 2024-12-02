
#smallest sum subarray
def main(array:list[int])->int:
    
    n=len(array)
    maximum=float("-inf")
    
    for start in range(n):
        
        for end in range(start+1,n):
            
            substring=array[start:end+1]
            
            if len(substring) >=2:
                
                new=sorted(substring)

                smallest=new[0]
                smallest_second=new[1]
                
                total = smallest + smallest_second
                
                maximum=max(maximum,total)

    return maximum

arr = [3, 2, 1]
print(main(arr))