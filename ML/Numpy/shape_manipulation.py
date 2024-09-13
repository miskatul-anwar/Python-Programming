import numpy as np

a = np.array([
    [1,3,2],
    [1,2,3],
    [1,3,2],
    [1,2,3],
    ])

a = a.reshape((2,6))
print(a)
print('-'*10)
a = a.reshape((2,3,2))
print(a)

print(a.flatten())

# transpose function
print(a.transpose())


