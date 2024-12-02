from numpy.ma.core import maximum


def main(array):

    n=len(array)

    if n==0 :

        return  0

    if n==1:

        return  array[0]

    if n==2:

        return  max(array[0],array[1])

    def max_loot(start,end):

        money=0

        for i in range(start,end):

            current= array[i]

            for j in range(i+2,n):

                current += array[j]

            money =max(money,current)

        return  money

    scene1=max_loot(0,n-1)
    scene2=max_loot(1,n)

    return  max(scene1,scene2)

houses = [1 ,3 ,2 ,1]
print(main(houses))