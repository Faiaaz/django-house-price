import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("house_prices.csv")

# Prepare features and target
X = data[["area", "bedrooms"]]
y = data["price"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved!")
