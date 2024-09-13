import pandas as pd
from matplotlib import pyplot as plt

data2 = {
    "SSN": [123, 445, 541, 872],
    "Name": ["Anna", "Bob", "Jhon", "Mike"],
    "Age": [29, 81, 23, 43],
    "Height": [176, 120, 130, 167],
    "Gender": ["f", "m", "m", "m"],
}

data1 = {
    "SSN": [123, 445, 541, 872],
    "Name": ["Anna", "Bob", "Jhon", "Mike"],
    "Age": [29, 81, 23, 43],
    "Height": [176, 120, 130, 167],
    "Gender": ["f", "m", "m", "m"],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df = pd.merge(df1, df2)
print(df)
