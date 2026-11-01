import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Now we load the data
data = pd.read_csv("dataset/housing.csv")

#let's create a histogram

plt.figure(figsize =(8,5))
plt.hist(data["Price"], bins=30)

plt.title("Distribution of house prices")
plt.xlabel("Price")
plt.ylabel("Number of houses")

plt.show()

#Scatter Plot

plt.figure(figsize =(8,5))

plt.scatter(data["Avg. Area Income"], data["Price"])

plt.xlabel("Average Area Income")
plt.ylabel("Price")
plt.title("Income vsPrice")

plt.show()



#Correlation Matrix

print("Creating heatmap...")

numeric_data = data.drop("Address", axis=1)

print(numeric_data.head())

plt.figure(figsize=(10,8))

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")

plt.show()