
#pair with target sum

def main(array:list[int],target:int)->list[list[int]]:

    seen=set()
    r=[]

    for num in array:
        
        compliment  = target-num
        
        if compliment in seen:
            
            r.append([num,compliment])

        seen.add(num)

    return r

t=int(input("enter"))
arr=list(map(int,input().split()))

print(main(arr,t))


    
    