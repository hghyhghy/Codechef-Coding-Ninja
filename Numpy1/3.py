import numpy as np

a= np.array([[1,2],
             [3,4]])

print("First array",a)
b = np.array([[4, 3],
              [2, 1]])

print("Second Array",b)

# adding 1
print(f"Adding 1 to {a} becomes")
print(a+1)

print(f"substarcting 2 to {b} becomes")
print(b-2)

print(f"Sum of all elements from {a} is", a.sum())

print(f"Adding two array {a}, {b} is ", a+b)