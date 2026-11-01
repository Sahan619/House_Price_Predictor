import pandas as pd

# Now we load the data from CSV File
data = pd.read_csv('dataset/housing.csv')

# Show the first 5 rows
print("First 5 rows of the data set:")
print(data.head())

print("\n"+ "=" * 50)

# Show the information about the dataset
print("Dataset information :")
print(data.info())

print("\n" + "=" * 50)

# Show statistical summary of the dataset
print("Statistical summary of the dataset:")
print(data.describe())

print("\n" + "+" * 50)

#Check for missing values
print("Missing values in the dataset:")
print(data.isnull().sum())