import pandas as pd 

# df = pd.read_csv("C:\\Users\\DIGITAL_LAB_CSE\\Desktop\\advance-python\\insurance.csv")
df = pd.read_csv("C:/Users/DIGITAL_LAB_CSE/Desktop/advance-python/insurance.csv")

print(df.columns)
# print(df.head())
print(df.isna().sum().sum())
print(df['smoker'][df['smoker'].isna()])
print(df.iloc[0, :])
df = df.dropna()
# print(df.isna().sum().sum())

print(df.describe())

print(df.groupby('gender')['charges'].sum())
print(df.groupby('gender')['bmi'].sum())

print(df.groupby('gender')['charges'].max())
print(df.groupby('gender')['bmi'].max())



print(df['gender'].nunique())
print(df['smoker'].nunique())
print(df['region'].nunique())

print(df['gender'].value_counts())
print(df['smoker'].value_counts())
print(df['region'].value_counts())

df['smoker'].replace(['yes', 'no'], [1, 0], inplace=True)
df['gender'].replace(['female', 'male'], [1, 0], inplace=True)
df['region'].replace(
    ['southeast', 'northwest', 'northeast', 'southwest'], 
    [0, 1, 2, 3], 
    inplace=True
)
print(df.head())

numpy_array = df.to_numpy()
print(numpy_array.shape)

print(df.groupby('gender')['smoker'].sum())

print(df.head())

# Sorting
df = df.sort_values('age', ascending=True)
df.reset_index(drop=True, inplace=True)
# df = df.reset_index(drop=True)
print(df.head())

print(df.loc[0, :])  # based on index
print(df.iloc[0, :]) # row position => updated
