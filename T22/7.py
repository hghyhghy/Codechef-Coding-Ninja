

# A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time

# You are required to implement the following function.

# Int NumberOfCarries(int num1 , int num2);

# The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

def counting_carry(n1,n2):

    nu1=str(n1)
    nu2=str(n2)


    carry=0
    count=0

    p1=len(nu1) -1
    p2=len(nu2) -1

    while p1>=0 and p2>=0:

        digit1=int(nu1[p1]) if p1>=0 else 0
        digit2=int(nu2[p2]) if p2>=0 else 0

        total= digit1+digit2+carry

        if total > 9:

            carry = 1
            count += 1

        else:

            carry = 0


        p1 -= 1
        p2 -= 1

    return count

Num1= 451
Num2= 349

print(counting_carry(Num1,Num2))
