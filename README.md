# 🏠 House Price Predictor

A Machine Learning web application that predicts house prices based on different property and area characteristics.

The project uses Multiple Linear Regression and Flask to provide predictions through a simple web interface.

---

## 📌 Project Overview

This project demonstrates a complete Machine Learning workflow:

- Data exploration
- Data visualization
- Data preprocessing
- Feature selection
- Model training
- Model evaluation
- Model serialization
- Flask deployment
- Web-based predictions

The trained Machine Learning model predicts the estimated house price based on:

- Average Area Income
- Average Area House Age
- Number of Rooms
- Number of Bedrooms
- Area Population

---

## 🛠️ Technologies Used

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Multiple Linear Regression

### Data Visualization

- Matplotlib
- Seaborn

### Web Application

- Flask
- HTML
- CSS

### Model Deployment

- Joblib

---

## 📊 Dataset

The dataset contains 5,000 house records with information about:

| Feature | Description |
|---|---|
| Avg. Area Income | Average income of the area |
| Avg. Area House Age | Average age of houses in the area |
| Avg. Area Number of Rooms | Average number of rooms |
| Avg. Area Number of Bedrooms | Average number of bedrooms |
| Area Population | Population of the area |
| Price | House price |
| Address | Property address |

The `Address` column is removed before training because it is not directly used as a numerical feature by the model.

---

## 🧠 Machine Learning Model

The project uses **Multiple Linear Regression**.

The model learns the relationship between several input features and house prices.

### Input Features

```text
Average Area Income
Average Area House Age
Average Area Number of Rooms
Average Area Number of Bedrooms
Area Population