import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Load the full dataset
df = pd.read_csv("/Users/thanhtrung/UIT/MLOPS/ThucHanh/LAB02-API-Dockers/dataset/diabetes_binary_health_indicators_BRFSS2015.csv")

# 2. Split into 80% train / 20% test (stratify on the target to keep class balance)
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["Diabetes_binary"]
)

# 3. Save the test set for later API testing
test_df.to_csv(
    "test_diabetes_binary_health_indicators_BRFSS2015.csv",
    index=False
)

print(f"Total: {len(df)} rows → Train: {len(train_df)} rows, Test: {len(test_df)} rows")
