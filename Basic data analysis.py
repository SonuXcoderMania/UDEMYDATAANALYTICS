import pandas as pd
import numpy as np

data=pd.DataFrame({
    'Name':['sonu','monu','sugam'],
    'Age':[25,25,96],
    'Salary':[22232,52611,525]
})
print(data.head())# this command used print head(means starting info) of the dataset
print(data.describe())#it will used show summary (mean ,mode etc)
filtered_data=data[data['Age']>45]
print(filtered_data)