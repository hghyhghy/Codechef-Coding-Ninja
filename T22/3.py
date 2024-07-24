
# You are given a function.
# int CheckPassword(char str[], int n);
# The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.

# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number
# Assumption:
# Input string will not be empty


def password_checker(password):

    if len(password) < 4:

        return 0
    
    upper=False
    digit=False

    for char in password:

        if char.isupper():

            upper=True
        elif char.isdigit():

            digit=True

        
    if char == " " or char == "/":

            return 0
        
    if password[0].isdigit():

            return 0
        
    if digit and upper:

            return 1
        
    else:

            return 0
        

password1 = "Passw0rd" 

print(password_checker(password1))
        

