# Machine Leaning Ultimate Roadmap

Comming up...
![[Screenshot_20240624_111736.png]]
***
## Chapter 01 (Maths)
![[Pasted image 20240624113714.png]]

Maths will be the foundation what you'll need the most in this journey!
The most important topics are...

![[Pasted image 20240624113826.png]]

The recomended _Youtube_ Channel: https://www.youtube.com/@3blue1brown
Khan Academy: https://www.khanacademy.org/math

- Differential Equations: https://youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6&si=e7turRZbKMwug3_a
- Calculus: https://www.youtube.com/playlist?list=PL0-GT3co4r2wlh6UHTUeQsrf3mlS2lk6x
- Linear Algebra: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- Linear Transformations and matricies: https://youtu.be/kYB8IZa5AuE?si=CllsLSxv1mRSOMs-
- Probability: https://youtube.com/playlist?list=PLiAulSm0XXgvCGe63mrAkda9UQ9478YQv&si=ak2e13qpELSLI706 
***
## Chapter 02 (Python)
![[Pasted image 20240624120542.png]]
video link to a free course: https://youtu.be/rfscVS0vtbw?si=kzvxDIa05XAOnraL

Just try to learn the basics of python and that's it. Don't try to deep dive.
In 2024, learning something has become really easy. Understand the basics, keep your eye on the goal.
***
## Chapter 03 (Data Analysis)
![[Pasted image 20240624121021.png]]

Some important _python_ libraries for 'Data Analysis'...
- Numpy
- Pandas
- Matplotlib
### Numpy
![[Pasted image 20240624121354.png]]

Numpy will help you with numbers, arrays, matrices, mathematical constants and functions etc.
![[Pasted image 20240624121838.png]]
### Pandas
![[Pasted image 20240624121427.png]]

Pandas will help you with any data that is stored in tabular form. One of them is CSV format. Now, what's a csv file?
![[Pasted image 20240624122322.png]]

Let's visualize one...
![[Pasted image 20240624122038.png]]

### Matplotlib
![[Pasted image 20240624121644.png]]

Once you run the model, you've some outcomes & probabilites. You might need to showcase it. That's where _matplotlib_ comes in.
![[Pasted image 20240624122644.png]]

*Let's Start With Some Basic **Plotting** Examples: 
```python
from numpy import *
from pylab import *

x = arange(-10, 10, 0.5)
y = x**2
plot(x, y, "r.")
show()

```
#### Histogram
```python
import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
categories = ["A", "B", "C", "D"]
values = [10, 23, 17, 5]
ax = plt.bar(categories, values)
plt.xlabel("marks", font="Maple Mono")
plt.ylabel("marks", font="Maple Mono")
plt.title("CSE 116 Marks", font="Maple Mono")
plt.legend("CSE116", loc="lower left")
# ax.bar(langs, students)
plt.show()
```

#### Graphs
##### f(x) = sin(x)
```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes()

# Plot for f(x) = sin(x)
# let's consider, y = f(x) = sin(x)

x_data = np.arange(0, 20, 0.1)
y_data = np.sin(x_data)

ax.set_title("f(x) = sin(x)", font="Maple Mono", color="red")
ax.set_xlabel("sin(x)")
ax.set_ylabel("sin(x)")
ax.plot(x_data, y_data)
plt.show()

```

#### 3D
##### Sphere
```python
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

# Create a sphere using numpy
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(v), np.sin(u))
y = np.outer(np.sin(v), np.sin(u))
z = np.outer(np.ones(np.size(u)), np.cos(u))
ax.plot_surface(x, y, z, color="r", rstride=4, cstride=4)

plt.show()

```
##### Scatter Plot
###### 01
```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

x_data = np.arange(0, 10, 0.1)
y_data = np.arange(0, 10, 0.1)
z_data = x_data * y_data

# ax.scatter(x_data, y_data, z_data, alpha=0.5, color="black")
ax.plot(x_data, y_data, z_data)

plt.show()

```
##### 02
```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

x_data = np.arange(0, 100, 10)
y_data = np.arange(0, 100, 10)
z_data = np.arange(0, 100, 10)

ax.scatter(x_data, y_data, z_data, color="red", marker="v", alpha=0.9)

plt.show()

```
##### Surface Plot
```python
import matplotlib.pyplot as plt
import numpy as np

myplot = plt.axes(projection="3d")

x_data = np.arange(0, 20, 0.1)
y_data = np.arange(0, 20, 0.1)
X, Y = np.meshgrid(x_data, y_data)
Z = X * Y

myplot.plot_surface(X, Y, Z)
plt.show()

```
***
## Chapter 04 (Frameworks)
There are tons of frameworks for _Machine Learning_
![[Pasted image 20240624123039.png]]

Among them, most popular ones are...
- Advanced \
  - TensorFlow
- Beginner Friendly
  - Pytorch (recommended)
  - Scikit-learn

I'll be focusing on _pytorch_ ...
- Brief intro to _pytorch_ : https://youtu.be/ORMx45xqWkA?si=vkXr5l5BKgKHiVQS
- _pytorch_ full course: https://youtu.be/V_xro1bcAuA?si=QGptWEj2G96JislG

_Machine Leaning Full Course: _ https://www.coursera.org/specializations/machine-learning-introduction

_ML Based Free Projects_
Flappy Bird: https://youtube.com/playlist?list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&si=SWIvFeLUvSsR08dA

Let's discuss about Types of Machine Learning,
- Supervised
- Unsupervised
- Reinforcement
## Supervised ML

Types of Supervised ML,
- Regression Problem
  - logistic
  - polynomial
  - classification
  - K-nearest
  
- Classification Problem

![[Pasted image 20240624123957.png]]

## Unsupervised ML
![[Pasted image 20240624124140.png]]

## Reinforcement ML
![[Pasted image 20240624124053.png]]

Demo project on Reinforcement ML
![[Pasted image 20240624124301.png]]

The charracter in the game will auto matically learn how to walk...
![[Pasted image 20240624124346.png]]

***
## Chapter 05 (Practice)
Start solving problems: https://www.kaggle.com/datasets

A famous data set called "The Titanic Dataset" is the best choice for the beginners...
![[Pasted image 20240624125456.png]]

Also watch out, 
CIFAR 10: https://www.cs.toronto.edu/~kriz/cifar.html
![[Pasted image 20240624125649.png]]

EMNIST: https://www.kaggle.com/datasets/crawford/emnist
![[Pasted image 20240624125807.png]]

### What's Neural Network ?
![[Pasted image 20240624125930.png]]

A free course on Neural Network !
![](https://i.ytimg.com/vi/VMj-3S1tku0/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLChyxrlO8apEF00Y6TnKYY5Rpg8gQ)

Neural Networks: Zero to Hero
https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&pp=iAQB

Some Buzz words..
![[Pasted image 20240624130307.png]]

Another Robust course...
![](https://i.ytimg.com/vi/gR8QvFmNuLE/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD8nXNULAALCXMeaxrp20FSgDvh2g)

CS50's Introduction to Artificial Intelligence with Python 2023
https://www.youtube.com/watch?v=gR8QvFmNuLE&list=PLhQjrBD2T381PopUTYtMSstgk-hsTGkVm&pp=iAQB

The Big picture of Neural Network:
![[Pasted image 20240624130607.png]]

More Topics Related to _Machine Learning_...
![[Pasted image 20240624130711.png]]

NLP Free course by _Hugging Face_ : https://huggingface.co/learn/nlp-course/

***

## Chapter 06 (Learn Generative AI)

Materials Related to this chapter,
- GPT Documentation
- ChatGPT short courses (search google)
- GPT store
***

###### Thank You