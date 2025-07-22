# Spam Classification with UCI Spambase Dataset

This project classifies emails as spam or not spam using machine learning algorithms and the UCI Spambase dataset.

## Project Structure

```
project/
├── src/
│   ├── add_header.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── requirements.txt
├── README.md
└── .gitignore
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

## Example Output

```
Evaluation Results:
Accuracy:  0.9457
Precision: 0.9484
Recall:    0.9118
F1-score:  0.9298
```

## Dataset Source
- [UCI Spambase Dataset](https://archive.ics.uci.edu/dataset/94/spambase)

## License
This project uses the UCI Spambase dataset, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
