import pandas as pd 

dataframe = pd.read_csv("diabetes.csv", delimiter=',')

print(dataframe.head())
print(dataframe.describe())
print(dataframe['Age'].max())

# get a specific data
print(dataframe['Age'][50])
print(dataframe.loc[50, 'Age'])
print(dataframe.iloc[50, -2])
print(dataframe.iloc[50, :])

# Missing value
print(dataframe.isna().sum())
dataframe['Outcome'].isna()
print(dataframe['Outcome'][dataframe['Outcome'].isna()])

# Drop
# dataframe = dataframe.dropna()
# print(len(dataframe))
# Fill data
dataframe = dataframe.fillna(1)
print(dataframe.isna().sum())

# Adding new column
dataframe['Overaged'] = dataframe['Age'] > 50 
print(dataframe.columns)

print(dataframe.head())

# Changing data type
dataframe['Overaged'] = dataframe['Overaged'].astype(int)
print(dataframe.head())

# Rename column name
dataframe.rename(columns={'Overaged': 'Over Aged'},inplace=True)
print(dataframe.columns)

# Observation
print(dataframe[dataframe['Age'] > 70])
print(dataframe[dataframe['BMI'] > 35])

# Plotting
from matplotlib import pyplot

dataframe['BMI'].hist()
pyplot.show()

# Saving 
dataframe.to_csv("diabetes-modified.csv", sep=',')