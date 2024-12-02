


#longest increasing subsequence

def main(array):

    stack=[]
    for num in array:

        if not stack or stack[-1] < num:

            stack.append(num)

        else:

            for i in range(len(stack)):

                if stack[i] > num:

                    stack[i]=num
                    break

    return  len(stack)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(main(arr))