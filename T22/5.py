
# def ProductSmallestPair(sum, arr)

# The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair

# NOTE

# Return -1 if array is empty or if n<2
# Return 0, if no such pairs found
# All computed values lie within integer range


def finding_least_pair(sum,arr):

    if not arr or len(arr) < 2:

        return -1
    
    n=len(arr)
    temp_store=[]

    for i in range(n):

        for j in range(i+1,n):

            if arr[i] + arr[j] <= sum:

                temp_store.append([arr[i],arr[j]])


    least=min(temp_store)
    return least,least[0]*least[1]


sum=9
arr=[5 ,2 ,4 ,3 ,9 ,7 ,1]
print(finding_least_pair(sum,arr))

