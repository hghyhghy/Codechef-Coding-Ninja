

#four sum latest

def main(array):

    n=len(array)
    store=[]

    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                for l in range(k+1,n):

                    if (array[i]+array[j]+array[k]+array[l]) == 0:

                        store.append([array[i],array[j],array[k],array[l]])

    return  store

nums = [1, 0, -1, 0, -2, 2]
print(main(nums))