
#longest palindromic substring

def check(array):
    
    return array==array[::-1]

def main(array):
    
    n=len(array)
    max_lenght=float("-inf")
    r=[]

    for i in range(n):
        
        for j in range(i,n):
            
            substring=array[i:j+1]
            if check(substring):
                
                length =j-i+1
                
                if length > max_lenght:
                    
                    max_lenght =  length
                    r=substring
                    
    return r

arr = [1, 2, 3, 2, 1, 4, 5, 4, 2, 1]
print(main(arr))