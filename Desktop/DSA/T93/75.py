#merge two sorted array

def main(arr1,arr2):

    a=len(arr1)
    b=len(arr2)

    i=a-1
    j=b-1
    
    r=[]
    carry=0

    while i>=0 or j>=0 or carry >0:
        
        d1=arr1[i] if i>=0 else 0
        d2=arr2[j] if j>=0 else 0
        
        total = d1+d2+carry
        
        carry =total//10
        remainder=total%10
        
        r.append(remainder)

        i-=1
        j-=1
        
    return r[::-1]

ar1=list(map(int,input().split()))
ar2=list(map(int,input().split()))

print(main(ar1,ar2))

    
    