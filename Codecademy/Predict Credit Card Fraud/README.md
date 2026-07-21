# Credit Card Fraud Detection

A machine-learning pipeline for identifying potentially fraudulent credit-card transactions. The project demonstrates data exploration, preprocessing, class-imbalance analysis, model training, and performance evaluation.

## Project Objective

Credit-card fraud detection is an imbalanced classification problem because fraudulent transactions represent a small portion of the complete dataset.

This project evaluates machine-learning methods using metrics that reflect fraud-detection performance rather than relying only on overall accuracy.

## Features

- Exploratory data analysis
- Missing-value and duplicate analysis
- Feature preprocessing
- Class-distribution analysis
- Train and test data separation
- Classification-model training
- Precision, recall, F1, and ROC-AUC evaluation
- Confusion-matrix visualization
- Reproducible Python environment

## Technology Stack

- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Workflow

```mermaid
flowchart TD
    DATA[Transaction Data] --> EDA[Exploratory Analysis]
    EDA --> PRE[Preprocessing]
    PRE --> SPLIT[Train-Test Split]
    SPLIT --> MODEL[Model Training]
    MODEL --> EVAL[Model Evaluation]
    EVAL --> RESULT[Fraud Predictions]
```

## Repository Structure

```text
credit-card-fraud-detection/
├── data/
│   └── README.md
├── notebooks/
│   └── fraud_detection_analysis.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── evaluate.py
├── reports/
│   └── figures/
├── .gitignore
├── README.md
└── requirements.txt
```

## Evaluation Metrics

Because the dataset is imbalanced, accuracy alone can be misleading.

The analysis focuses on:

- Precision
- Recall
- F1 score
- ROC-AUC
- Confusion matrix

| Model | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|
| [Model name] | [Result] | [Result] | [Result] | [Result] |
| [Model name] | [Result] | [Result] | [Result] | [Result] |

Replace placeholders with actual measured results. Do not invent metrics.

## Installation

```bash
git clone https://github.com/ryanhihi/credit-card-fraud-detection.git
cd credit-card-fraud-detection
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter lab
```

## Dataset

The dataset is not stored directly in this repository if its license or size prevents redistribution.

Download it from:

```text
[INSERT OFFICIAL DATASET SOURCE]
```

Place it in:

```text
data/raw/
```

## Key Findings

- [Describe the most important class-imbalance observation.]
- [Identify the best-performing model.]
- [Explain the trade-off between precision and recall.]
- [Describe the most important limitations.]

## Limitations

- Results depend on the available dataset and its feature representation.
- Fraud patterns may change over time.
- Model performance on historical data does not guarantee production performance.
- A production system would require monitoring, retraining, security, and human-review processes.

## Future Improvements

- Compare additional classification models
- Add imbalance-handling techniques
- Add hyperparameter optimization
- Add explainability analysis
- Create a FastAPI inference endpoint
- Add automated training and evaluation tests
- Containerize the application

## Author

Ryan Tran  
[Portfolio](INSERT_LINK) | [LinkedIn](INSERT_LINK)
