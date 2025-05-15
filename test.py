import joblib

model = joblib.load("models/DecisionTree_model.pkl")
print("✅ Loaded model with joblib:", type(model))
