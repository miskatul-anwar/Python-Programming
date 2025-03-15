import numpy as np

a = np.array([
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    ])

for x in a.flat:
    print(x,end=' ')
print()
