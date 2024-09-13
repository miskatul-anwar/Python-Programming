from matplotlib import pyplot as plt
from matplotlib import style
# style.use('ggplot')
nationalities = [
    "Bangladeshi",
    "Canadian",
    "French",
    "Indian"
    ]

students = [10,
            13,
            89,
            120
            ]

pairs = zip(students,nationalities)
pairs = sorted(list(pairs))

students, nationalities = zip(*pairs)
print(pairs)
explode=[0,
         0,
         0,
         0.05]
plt.pie(students,labels=nationalities,autopct='%d',shadow=True,explode=explode,counterclock=False)
plt.title("Student Nationality")
plt.show()

