import joblib


def test_model_exists():
    model = joblib.load("model.joblib")

    prediction = model.predict([[4, 2, 2]])

    assert prediction[0] > 0