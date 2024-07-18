

# find quadruples 

def find_quadruples(arr, target):

    n=len(arr)

    temp=set()

    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                for l in range(k+1,n):

                    if  arr[i] + arr[j] + arr[k] + arr[l] == target:

                        store= tuple(sorted((arr[i],arr[j],arr[k],arr[l])))
                        temp.add(store)

    return list(temp) 

A = [1, 0, -1, 0, -2, 2]
K = 0
result = find_quadruples(A, K)
print(result)

