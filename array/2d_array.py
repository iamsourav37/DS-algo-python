import numpy as np

array1 = np.array([
    [3, 4, 8],
    [2, 1, 3],
    [4, 8, 6],
])

array2 = np.array([
    [2, 3, 8],
    [5, 9, 4],
    [9, 8, 7],
])


# sum, sub, product of two matrix

sum = np.zeros([3, 3], dtype=int)
sub = np.zeros([3, 3], dtype=int)
product = np.zeros([3, 3], dtype=int)

for i in range(len(array1)):
    for j in range(len(array1)):
        sum[i][j] = array1[i][j] + array2[i][j]
        sub[i][j] = array1[i][j] - array2[i][j]
        product[i][j] = array1[i][j] * array2[i][j]



print(f"Sum of two matrix : {sum}")
print(f"Sub of two matrix : {sub}")
print(f"Product of two matrix : {product}")



