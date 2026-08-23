import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Housing.csv")



y=df["price"]
x=df[["bedrooms","bathrooms","stories"]]

model = LinearRegression()
model.fit(x,y)

joblib.dump(model,"model.joblib")

print("done")   