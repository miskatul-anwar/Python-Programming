import numpy as np

a = np.array([
    [1,3,2],
    [1,2,3],
    [1,3,2],
    [1,2,3],
    ])

print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.exp(a))
print(np.log(a))

print(np.sin(0))
print(np.cos(0))

c = np.array([1,1,1,1])
print(np.sum(c))

d = np.array([1,1,2,1])
print(np.mean(d))
print(np.median(d))

# standard deviation
print(np.std(d))

# concat two arrays
x = np.array([1,1,1,1])
y = np.array([2,2,2,2])
c = np.concatenate((x,y))
print(c)

print()
# horizontal stack
c = np.hstack((x,y))
print(c)

print(np.split(c,4))
# vertical stack
c = np.vstack((x,y))
print(c)

# linear array
b = [10,20,30,40]
# a = np.insert(a,1,b,axis=0)
print(b)
