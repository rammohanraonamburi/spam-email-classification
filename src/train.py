import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data_dir="data", model_dir="models"):
    X_train = pd.read_csv(os.path.join(data_dir, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(data_dir, "y_train.csv")).values.ravel()
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "spam_classifier.pkl")
    joblib.dump(clf, model_path)
    print(f"Model saved to {model_path}")
    return model_path

if __name__ == "__main__":
    train_model() 