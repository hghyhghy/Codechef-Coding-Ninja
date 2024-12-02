

#minimum cost  array 

def main(array):
    
    cost1=0
    cost2=0
    n=len(array)
    non_decreasing = sorted(array)
    non_increasing= sorted(array,reverse=True)

    for i in range(n):
        
        cost1 += abs(array[i]-non_decreasing[i])
        
    for j in range(n):
        
        cost2 += abs(array[i]-non_increasing[i])

    
    return min(cost1,cost2)

num= list(map(int,input().split()))
print(main(num))