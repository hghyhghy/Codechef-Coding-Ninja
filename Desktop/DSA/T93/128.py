
#kth largest element

import heapq

def main(array,k):
    
    extracted= array[:k]
    heapq.heapify(extracted)

    for num in array[k:]:

        if num > extracted[0]:
            
            heapq.heappop(extracted)
            heapq.heappush(extracted,num)

    return extracted[0]

k=2
num=list(map(int,input().split()))

print(main(num,k))
        
        