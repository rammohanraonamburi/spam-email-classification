# Spam Classification with UCI Spambase Dataset

This project classifies emails as spam or not spam using machine learning algorithms and the UCI Spambase dataset.

## Project Structure

```
your_project/
├── data/                  # For raw and processed data files
├── models/                # Saved models
├── src/
│   ├── data_loader.py     # Downloading and loading the dataset
│   ├── preprocess.py      # Data cleaning and preprocessing
│   ├── train.py           # Model training
│   └── evaluate.py        # Model evaluation
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Download and save the dataset:
   ```bash
   python src/data_loader.py
   ```

3. Preprocess and split the data:
   ```bash
   python src/preprocess.py
   ```

4. Train the model:
   ```bash
   python src/train.py
   ```

5. Evaluate the model:
   ```bash
   python src/evaluate.py
   ```

## Dataset Source
- [UCI Spambase Dataset](https://archive.ics.uci.edu/dataset/94/spambase)

## License
This project uses the UCI Spambase dataset, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). 