import pandas as pd
from matplotlib import pyplot as plt 

series = pd.Series([10,20,30,40],['A','B','C','D']) 
series1= pd.Series([10,20,30,40],['A','B','C','D']) 
series2= pd.Series([10,20,30,40],['A','B','C','D']) 
series.name = "My series"
print(series)
print(dict(series))
print(series1+series2)
print(series2.tail(2))

def sq(x:int)->None:
    return x**2

print(series2.apply(sq))

print(series2.sort_index)
# print(series2.sort_values(implace=True))  to apply the change use impace

series.plot.bar()
plt.show()

# create a csv file
 
series.to_csv('series.csv')