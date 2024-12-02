# Problem statement
# During Endgame Natasha(Black Widow) sacrificed her life for the soul stone.

# Hulk wants to bring Natasha back. So, he came to Goku for help. Goku told him he will help Hulk if he can solve the task given by him. Hulk accepts the challenge of Goku.

# Goku gave Hulk a list of ‘N’ numbers and a number ‘K’. The task is to rearrange the elements of the list such that all elements less than or equal to ‘K’ become adjacent to each other. Hulk can only swap any two elements of the array/list multiple times. Goku wants Hulk to do the task using the minimum number of swaps.

# As Hulk is not good at maths so he called you to solve the task given by Goku to save Natasha.The fate of Natasha lies in your hand.

def minimum_swaps_needed(array:list[int],k:int)->int:
    
    n=len(array)
    swaps=0
    j=0
    
    for i in range(n):
        
        if array[i]<=k:
            
            if  i != j:
                
                array[i],array[j]=array[j],array[i]
                
                swaps += 1
                
            j +=1
            
    return swaps

arr = [2, 1, 5, 6, 3]
K = 3
print(minimum_swaps_needed(arr,K))