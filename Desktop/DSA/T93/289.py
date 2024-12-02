

def main(array,left,right):
    
    max_loot= 0
    
    for i in range(left,right):

        current = array[left]

        for j in range(i+2,right):
            
            current += array[j]

            max_loot=max(max_loot,current)

    return max_loot

s1=main(array,0,n-1)
s2=main(array,1,n)

return max(s1,s2)