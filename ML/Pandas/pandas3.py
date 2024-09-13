import pandas as pd
from matplotlib import pyplot as plt

data = {
    'SSN' : [123,445,541,872],
    'Name':['Anna','Bob','Jhon','Mike'],
    'Age': [29,81,23,43],
    'Height': [176,120,130,167],
    'Gender' :['f','m','m','m']
}

df = pd.DataFrame(data)
print(df['Age'].sum())
print(df['Age'].prod()) # multiply all
print(df['Height'].mean())
print(df['Height'].median())
print(df['Height'].mode()) # which appears the most ?
print(df['Height'].std())
print(df['Height'].min())
print(df['Height'].max())
print(df['Height'].describe())