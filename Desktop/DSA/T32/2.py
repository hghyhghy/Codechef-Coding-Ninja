# You have been given two arrays/list ‘ARR1’ and ‘ARR2’ consisting of ‘N’ and ‘M’ integers respectively. Your task is to return the number of elements common to ‘ARR1’ and ‘ARR2’ and the number of elements in the union of ‘ARR1’ and ‘ARR2’.

def count_common_elements(a1,a2):
    
    count= 0
    i=0
    j=0
    
    while i<len(a1) and j < len(a2):
        
        if a1[i] == a2[j]:
            
            count += 1
            i += 1
            j += 1
            
        elif a1[i] < a2[j]:
            
            i += 1
            
        else:
            
            j += 1
            
            
    return count


ARR1 = [1, 2, 4, 5, 6]
ARR2 = [2, 5, 7, 9]

print(count_common_elements(ARR1,ARR2))