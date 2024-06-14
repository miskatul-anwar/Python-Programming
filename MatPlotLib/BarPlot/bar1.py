import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
ax = plt.bar()
langs = ["C", "C++", "Java", "Python", "PHP"]
students = [23, 17, 35, 29, 12]
# ax.bar(langs, students)
ax.plot(langs, students)
plt.show()
