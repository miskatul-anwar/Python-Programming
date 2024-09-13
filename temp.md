# Machine Leaning Ultimate Roadmap

Comming up...

Table of contents...

- Maths
- Python
- Data Analysis
- Framework
- Practice
- Learn Generative AI

---

## Chapter 01 Maths

Maths will be the foundation what you'll need the most in this journey!
The most important topics are...

    The recomended _Youtube_ Channel: https://www.youtube.com/@3blue1brown

Khan Academy: https://www.khanacademy.org/math

- Differential Equations: https://youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6&si=e7turRZbKMwug3_a
- Calculus: https://www.youtube.com/playlist?list=PL0-GT3co4r2wlh6UHTUeQsrf3mlS2lk6x
- Linear Algebra: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- Linear Transformations and matricies: https://youtu.be/kYB8IZa5AuE?si=CllsLSxv1mRSOMs-
- Probability: https://youtube.com/playlist?list=PLiAulSm0XXgvCGe63mrAkda9UQ9478YQv&si=ak2e13qpELSLI706

### Probability

#### Bayes Theorem, The geometry of changing beliefs

Develop Rational Thinking Capabilites...
Rationality: Recongnizing which facts are relevant

$$P(H|E) = \frac{P(H) \cdot P(E|H)}{P(E)}$$
$$P(H) = Probability \space a \space hypothesis \space is \space true$$
$$P(H)=Probability \space of \space  seeing \space the \space evidence \space if \space  the\space  hypothesis \space is \space true $$
$$P(E) = Probability \space of \space seeing \space the \space evidence$$
$$P(H|E) = Probability \space a \space hypothesis \space is \space true $$

The "|" stands for 'given'
$$P(H|E)  = P (Hypothesis \space given \space Evidence) $$
Also,
$$P(H|E)=\frac{P(H\cap E)}{P(E)}$$
$$P(E)P(H|E)=P(H \cap E)=P(H)P(E|H)$$
Let's Investigate some problems,

- Steve is very shy and withdrawn invariably helpful but with very little interest in people or in the world of reality. A meek and tidy soul, he has a need for order and structure, and a passion for detail. What's he?
- [] A Librarian
- [x] A Farmer

where did the values came from ?

Prior, Possibility of being a librarian, P(H) = 1 / 21
Limit your view, P(E|H) = 0.4 means , About 40% Librarian fits this criteria
This thing also known as 'Likelihood'
Number of librarians = Total number of people \* the prior probability of being a librarian

On the other hand, P(E|¬H) = 0.1

The formulae applies as below,

<u>Exercise 01:</u>
Probabiliy a 4 comes up in a dice roll given the result is an even number?
H = 4 comes up
E = The number is even
$$P(H|E) = \frac{1}{3} $$
OMG how did this happen ?
I've applied the byes theorem
$$P(A∣B)=\frac{P(B∣A)\cdot P(A)}{P(B)}​ $$

To solve this problem using Bayes' theorem, let's define the events and calculate accordingly.

Let:

- A: Event that a 4 comes up on a dice roll.
- B: Event that the result is an even number.

We want to find $$P(A \mid B)$$the probability that a 4 comes up given that the result is an even number.

Firstly, identify the relevant probabilities:

- The outcomes of a fair six-sided die are $$ \{1, 2, 3, 4, 5, 6\} $$.
- Even numbers on the die are {2, 4, 6} , so P(B) , the probability that the result is even, is $$ \frac{3}{6} = \frac{1}{2} $$

Now, calculate P(A), the probability that a 4 comes up:

- There is only 1 outcome of interest (4) out of 6 possible outcomes, so $$ P(A) = \frac{1}{6} $$

Next, calculate P(B|A) , the probability that the result is even given that a 4 comes up:

- Since a 4 is an even number, $$P(B \mid A) = 1$$

Now, apply Bayes' theorem:
$$ P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)} $$

Substitute the values we have calculated:
$$ P(A \mid B) = \frac{1 \cdot \frac{1}{6}}{\frac{1}{2}} = \frac{\frac{1}{6}}{\frac{1}{2}} = \frac{1}{6} \cdot \frac{2}{1} = \frac{1}{3}$$

Therefore, the probability that a 4 comes up in a dice roll given that the result is an even number is $$ \frac{1}{3} $$

<u>Exercise 02:</u>
Suppose a rare disease affects 1 in 10,000 people in a population. There exists a test for this disease that is 99% accurate for both positive and negative results. If a person tests positive for the disease, what is the probability that they actually have the disease?

Let's denote:

- DDD: Event that a person has the disease.
- TTT: Event that the test is positive.

We need to find $$P(D \mid T)$$the probability that a person has the disease given that the test is positive.

According to Bayes' theorem:

$$
P(D \mid T) = \frac{P(T \mid D) \cdot P(D)}{P(T)}
$$

1. **Prior probabilities:**

- P(D)=0.0001 (since the disease affects 1 in 10,000 people)
- P(¬D)=1−P(D)=0.9999

2. **Likelihoods:**

- P(T∣D)=0.999 (probability of a positive test given that the person has the disease)
- P(T∣¬D)=0.01 (probability of a positive test given that the person does not have the disease)

3. **Total probability of the test being positive:**
   $$P(T)=P(T \mid D)\cdot P(D)+P(T\mid¬D)\cdot P(¬D)$$
   $$P(T)=(0.99 \cdot 0.0001)+(0.01 \cdot 0.9999)$$
   $$P(T)=0.000099+0.009999$$
   $$P(T)=0.010098$$

4. **Applying Bayes' theorem:**
   $$P(D \mid T) = \frac{P(T \mid D) \cdot P(D)}{P(T)} $$
$$ P(D∣T)=\frac{0.99 \cdot 0.0001}{0.010098} $$
$$ P(D∣T)=\frac{0.010098}{0.000099} $$
$$ P(D∣T)≈0.00980392 $$

So, if a person tests positive for the disease, the probability that they actually have the disease is approximately 0.98% (or 0.0098). This example illustrates how Bayes' theorem can be used to adjust the probability of an event (having the disease) given new evidence (a positive test result).

A problem collected from debashish
![[Pasted image 20240624195628.png]]
<u>Exercise 03:</u>
P(sick) = 10% = 0.1
P(pos|¬sick) = 0.05
P(neg|sick) = 0.01

solution:

$$
P(pos|sick) = 1-P(neg|sick) = 1-0.01=0.99=99 \%
$$

Now,
$$P(sick|pos)=\frac{P(pos|sick)\cdot P(sick)}{P(pos)}$$
let's extract the P(pos),
$$P(pos)=P(pos|sick)\cdot P(sick)+P(pos|¬sick)\cdot P(¬sick)$$
$$P(pos)=(0.99\cdot 0.10)+(0.05\cdot0.90) = 0.144$$
$$P(sick|pos)=\frac{0.99\cdot0.10}{0.144}=0.6875$$

<u>Exercise 04:</u>
Radar detection. If an aircraft is present in a certain area, a radar correctly registers its presence with probability 0.99. If it is not present, the radar falsely registers an aircraft presence with probability 0.10. We assume that an aircraft is present with probability 0.05. What is the probability of false alarm(a false indication of aircraft presence), and the probability of missed detection(nothing registers, even though an aircraft is present)?
Let's assume that
A = {an aircraft is present},
B = {the radar registers an aircraft presence},

Based on them we may find,
A<sup>c</sup> = {an aircraft is not present},
B<sup>c</sup> = {the radar does not register an aircraft presence}.
$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$
$$P(B)P(A|B)=P(A \cap B)=P(A)P(B|A)$$
Calculate the needed values,
$$P(A^c)=1-P(A)=1-0.05=0.95 $$
$$According~to~the~question,~P(B|A^c)=0.1$$
$$P(B|A)=0.99, ~Given~that~P(B^c|A)=1-0.99=0.01$$
$$P(false \space alarm) = P(A^c ∩ B) = P(A^c)P(B | A^c ) = 0.95 · 0.10 = 0.095$$
$$P(missed \space detection) = P(A ∩ B^c ) = P(A)P(B^c | A) = 0.05 · 0.01 = 0.0005$$

---

## Chapter 02 (Python)

video link to a free course: https://youtu.be/rfscVS0vtbw?si=kzvxDIa05XAOnraL
playlist (if you prefer): https://youtube.com/playlist?list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm&si=2mE3gQfgFJAjnbJ3

Just try to learn the basics of python and that's it. Don't try to deep dive.
In 2024, learning something has become really easy. Understand the basics, keep your eye on the goal.

---

## Chapter 03 (Data Analysis)

Some important _python_ libraries for 'Data Analysis'...

- Numpy
- Pandas
- Matplotlib

### Numpy

Numpy will help you with numbers, arrays, matrices, mathematical constants and functions etc.

### Pandas

Pandas will help you with any data that is stored in tabular form. One of them is CSV format. Now, what's a csv file?

Let's visualize one...

### Matplotlib

Once you run the model, you've some outcomes & probabilites. You might need to showcase it. That's where _matplotlib_ comes in.

\*Let's Start With Some Basic **Plotting** Examples:

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

---

## Chapter 04 (Frameworks)

There are tons of frameworks for _Machine Learning_

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

## Unsupervised ML

## Reinforcement ML

Demo project on Reinforcement ML

The charracter in the game will auto matically learn how to walk...

---

## Chapter 05 (Practice)

Start solving problems: https://www.kaggle.com/datasets

A famous data set called "The Titanic Dataset" is the best choice for the beginners...
![[Pasted image 20240624125456.png]]

Also watch out,
CIFAR 10: https://www.cs.toronto.edu/~kriz/cifar.html

EMNIST: https://www.kaggle.com/datasets/crawford/emnist

### What's Neural Network ?

A free course on Neural Network !
![](https://i.ytimg.com/vi/VMj-3S1tku0/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLChyxrlO8apEF00Y6TnKYY5Rpg8gQ)

Neural Networks: Zero to Hero
https://www.youtube.com/watch?v=VMj-3S1tku0&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&pp=iAQB

Some Buzz words..

Another Robust course...
![](https://i.ytimg.com/vi/gR8QvFmNuLE/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD8nXNULAALCXMeaxrp20FSgDvh2g)

CS50's Introduction to Artificial Intelligence with Python 2023
https://www.youtube.com/watch?v=gR8QvFmNuLE&list=PLhQjrBD2T381PopUTYtMSstgk-hsTGkVm&pp=iAQB

The Big picture of Neural Network:

More Topics Related to _Machine Learning_...

NLP Free course by _Hugging Face_: https://huggingface.co/learn/nlp-course/
RNN by Lex Fridmen: https://youtu.be/nFTQ7kHQWtc?si=ZkFiX3XYr0a9YTMq

---

## Chapter 06 (Learn Generative AI)

Deep Learning Full Course: https://www.coursera.org/specializations/deep-learning

Materials Related to this chapter,

- GPT Documentation: https://platform.openai.com/docs/guides/text-generation
- ChatGPT short courses: https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
- GPT store: https://openai.com/index/introducing-the-gpt-store/

---

###### Thank You
