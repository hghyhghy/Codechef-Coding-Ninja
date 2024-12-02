
# You are required to implement the following function.

# Int OperationChoices(int c, int n, int a , int b )

# The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the function to return.

# ( a+ b ) , if c=1
# ( a – b ) , if c=2
# ( a * b ) ,  if c=3
# (a / b) ,  if c =4
# Assumption : All operations will result in integer output.

def OperationChoices(a,b,c):

    
    if c==1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:

        return a/b

    else:

        return None
    

c=1

a=12

b=16

print(OperationChoices(a,b,c))

