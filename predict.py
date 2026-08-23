import joblib

model = joblib.load("model.joblib")

bedrooms = float(input("Enter number of bedrooms: "))
bathrooms = float(input("Enter number of bathrooms: "))
stories = float(input("Enter number of stories: "))

prediction = model.predict([
    [bedrooms, bathrooms, stories]
])

print(f"Predicted house price: {prediction[0]:.2f}")  