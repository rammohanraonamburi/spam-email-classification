import os
import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_and_split(data_path="data/spambase.csv", output_dir="data", test_size=0.2, random_state=42):
    df = pd.read_csv(data_path)
    # Handle missing values (if any)
    df = df.dropna()
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    os.makedirs(output_dir, exist_ok=True)
    X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
    X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
    y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
    y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)
    print("Data split and saved to:", output_dir)

if __name__ == "__main__":
    preprocess_and_split() 