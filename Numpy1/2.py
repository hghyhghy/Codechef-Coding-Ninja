import numpy as np

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

print("Original Array is", arr)

print("Sliced array is")

sliced = arr[:2,::2]
print(sliced)