import pandas as pd
from matplotlib import pyplot as plt

data = {
    'SSN' : [123,445,541,872],
    'Name':['Anna','Bob','Jhon','Mike'],
    'Age': [29,81,23,43],
    'Height': [176,120,130,167],
    'Gender' :['f','m','m','m']
}

data_frame = pd.DataFrame(data)
data_frame.set_index('SSN', inplace=True)
data_frame['Age'].hist()
data_frame.plot()
print(data_frame)
print(data_frame.shape)
print(data_frame.dtypes)
print(data_frame.T) # get the Transpose version
data_frame.to_csv('dataframe.csv')
plt.show()