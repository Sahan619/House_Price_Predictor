import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import(
  mean_absolute_error,
  mean_squared_error,
  r2_score,

)
import joblib



#Now load the dataset
data =pd.read_csv("dataset/housing.csv")

#Remove the adress column

data = data.drop("Address", axis = 1)

# Definig X and Y

X = data.drop("Price", axis =1)
Y = data["Price"]


# Split the data
X_train , X_test , Y_train , Y_test = train_test_split(
     X,
     Y,
     test_size = 0.2,
     random_state =42,

)

# Create the model
model = LinearRegression()


#train the model
model.fit(X_train , Y_train)


# make predictions
predictions =model.predict(X_test)

# evaulate the model

mae = mean_absolute_error(Y_test , predictions)
mse = mean_squared_error(Y_test , predictions)
r2 = r2_score(Y_test, predictions)

print(f"Mean Absolute Error: {mae}")
print(f"mean Squared error: {mse}")
print(f"R2 Score: {r2}")

joblib.dump(model , "models/house_price_model.pkl")
print("Model Saved")


