# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

df = pd.read_excel("data/dataset.xlsx", sheet_name="Sheet1")

# check for null for each column
print(df.isnull().sum())

# Perpetrator Age has empty  spaces as vales
# Replace empty spaces with 0
df['Perpetrator Age'] = df['Perpetrator Age'].replace(' ', 0)

# convert Perpetrator Age column to int
df['Perpetrator Age'] = df['Perpetrator Age'].astype(int)

# Convert Victim Age column to int
df['Victim Age'] = df['Victim Age'].astype(int)

# Select  datta  when Perpetrator Age is greater than 5
# In United States the age for holding someone liable for a crime is 6 for some states
# We select data when Perpetrator Age is greater than 5
df = df[df['Perpetrator Age'] > 5]

# print the column types
print(df.dtypes)

# Convert dataframe to excel
df.to_csv("data/dataset_cleaned.csv", index=False)