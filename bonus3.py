import pandas as pd
data=pd.read_csv('heart_disease.csv')
print(data.isnull().sum())
data.dropna()