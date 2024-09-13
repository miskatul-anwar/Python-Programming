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
print(df['Height'].apply(lambda x:x*100))

for x in df['Age']:
    print(x)

# for key, value in df['Age'].iteritems():
 #   print("{}: {}".format(key,value))