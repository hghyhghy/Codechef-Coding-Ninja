
#merge sort

def main(string):
    
    n=len(string)

    if n<=1:
        return string
    
    mid=n//2
    
    left=main(string[:mid])
    right=main(string[mid:])

    return merge(left,right)


def merge(left,right):
    
    i=j=0
    r=[]

    while i<len(left) and j<len(right):
        
        if left[i]<=right[j]:
            
            r.append(left[i])

            i +=1
            
        else:
            
            r.append(right[j])

            j +=1
            
    
    r.extend(left[i:])
    r.extend(right[j:])

    return r

num=list(map(int,input().split()))
print(main(num))