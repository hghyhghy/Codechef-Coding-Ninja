# . Write a function to validate if the provided two strings are anagrams or not. If the two strings are anagrams, then return ‘yes’. Otherwise, return ‘no’.

def bubble_sort(arr):
    
    n=len(arr)

    for i in range(n-1):
        
        for j in range(n-i-1):
            
            if arr[j] > arr[j+1]:
                
                arr[j],arr[j+1]= arr[j+1],arr[j]

    return arr

def is_anagram(a1,a2):
    
    a1=a1.replace(" ","").lower()
    a2=a2.replace(" ","").lower()

    if len(a2) != len(a1):
        
        return "No"

    sorted1=bubble_sort(list(a1))
    sorted2=bubble_sort(list(a2))

    if sorted1 == sorted2:
        
        return "Yes "

    else:
        
        return "No"

print(is_anagram("Listen", "Silent")) 

