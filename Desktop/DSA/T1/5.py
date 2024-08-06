# The function accepts a string ‘str’ as its argument. The function needs to return the transformed string by replacing all occurrences of the character ‘a’ with the character ‘b’ and vice versa.

def transforemd_string(string):

   temp =""
   for i in range(len(string)):
      
        if string[i] == "b":

            temp += "a"

        elif string[i] == "a":

            temp += "b"

        else:

            temp += string[i]

   return temp
         

      

a="abaabbcc"
print(transforemd_string(a))

