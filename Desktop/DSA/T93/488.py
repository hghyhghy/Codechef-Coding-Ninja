#second largest element

def main(array):

    seen=set()
    n=len(array)
    r=[]
    for  num in array:

        if num not in seen:

            seen.add(num)
            r.append(num)


    new=sorted(r,reverse=True)
    return  new[1]

a=[2,1,2,4,5,5]
print(main(a))