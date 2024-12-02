# Problem statement
# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

# Hint : Use type casting

def fahrenheit_to_celcius(fahrenheit):
    
    celcius=(fahrenheit-32)*5/9

    return celcius

fahrenheit_temp = 100
print(fahrenheit_to_celcius(fahrenheit_temp))