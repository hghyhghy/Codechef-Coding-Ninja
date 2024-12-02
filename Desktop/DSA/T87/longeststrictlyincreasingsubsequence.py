# Problem statement
# 'N' students are standing in a row. You are given the height of every student standing in the row. Your task is to find the longest strictly increasing subsequence of heights from the row such that the relative order of the students does not change.

# A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.

def LIS(array:list[int])->int:
    
    stack=[]
    
    for num in array:
        
        if not stack or stack[-1] < num:
            
            stack.append(num)
            
        else:
            
            for i in range(len(stack)):
                
                if stack[i]> num:
                    
                    stack[i] = num
                    break
                
    return len(stack)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(LIS(arr))