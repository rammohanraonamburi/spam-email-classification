import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

def download_and_save_spambase(data_dir="../data"):
    os.makedirs(data_dir, exist_ok=True)
    spambase = fetch_ucirepo(id=94)
    X = spambase.data.features
    y = spambase.data.targets
    df = pd.concat([X, y], axis=1)
    csv_path = os.path.join(data_dir, "spambase.csv")
    df.to_csv(csv_path, index=False)
    print(f"Spambase dataset saved to {csv_path}")
    return csv_path

if __name__ == "__main__":
    download_and_save_spambase() 