
#reversing the stack

def main(array):

    temp = []

    while  array:

        temp.append(array.pop())


    return  temp

stack = [1, 2, 3, 4, 5]
print(main(stack))
