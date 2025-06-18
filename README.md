
---

### ✅ `README.md`

```markdown
# 📊 Week 3: End-to-End Insurance Risk Analytics & Predictive Modeling

This project is focused on analyzing and modeling insurance risk using real-world policy and claims data. The workflow follows a complete data science lifecycle: data ingestion, exploration, statistical hypothesis testing, modeling, and experiment tracking.

---

## 🚀 Project Structure

```

.
├── data/                         # DVC-managed data folder
│   ├── raw
    │   ├── MachineLearningRating_v3.csv
├── notebooks/                   # Jupyter notebooks per task
│   ├── Task1.ipynb
│   ├── Task_end.ipynb
├── scripts/                     # Modular Python scripts
├── src/                         # Source code package
├── tests/                       # Unit tests
├── .vscode/                     # Editor configuration
├── .github/workflows/          # GitHub Actions CI setup
├── .gitignore
├── dvc.yaml
├── README.md
└── requirements.txt

````

---

## 📂 Tasks Overview

### ✅ Task 1: Exploratory Data Analysis (EDA)
- Loaded raw text data using pandas and converted to CSV.
- Conducted univariate, bivariate, and multivariate analysis.
- Key risk metrics:
  - **Loss Ratio** = TotalClaims / TotalPremium
  - **Claim Frequency** = # of policies with claims / Total policies
  - **Claim Severity** = TotalClaims / # of policies with claims
- Plotted:
  - Province-level risk distributions
  - Premium & Claims trends
  - Outlier visualizations

### ✅ Task 3: Hypothesis Testing
Performed statistical validation on key risk factors:
- 🔍 **H₀: No risk difference across Provinces** → Rejected (p < 0.05)
- 🔍 **H₀: No risk difference between Zip Codes** → Rejected
- 🔍 **H₀: No margin difference by Zip Codes** → Accepted
- 🔍 **H₀: No gender-based risk difference** → Rejected

> Statistical tests: T-tests, ANOVA, and chi-squared depending on feature type.

### ✅ Task 4: Predictive Modeling
#### 🎯 Goals
- Predict claim **severity** (TotalClaims) → Regression
- Predict risk-adjusted **premium** → Future work

#### 🔧 Model Implemented
- `LinearRegression` (Baseline)
- Feature encoding & missing value imputation applied.
- Metrics used: **RMSE**, **R²**

> Further model tuning, ensemble models, and SHAP-based interpretability planned in next phase.

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/doffn/week-3-End-to-End-Insurance-Risk-Analytics-Predictive-Modeling.git
cd week-3-End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Data Version Control (DVC)

### Initialize DVC (already done)

```bash
dvc init
```

### Pull Raw Data

```bash
dvc pull
```

### Track New Data

```bash
dvc add data/raw/insurance_data.csv
git add data/raw/insurance_data.csv.dvc .gitignore
git commit -m "Track insurance data with DVC"
```

---

## 📈 Git Workflow

### Create Task Branch

```bash
git checkout -b task-3
```

### Commit & Push

```bash
git add .
git commit -m "Task 3: Hypothesis testing completed"
git push --set-upstream origin task-3
```

---

## ✅ CI/CD

GitHub Actions is configured to run unit tests on each push to `main` or pull request.

```yaml
.github/workflows/unittests.yml
```

---

## 📚 Requirements

```
pandas
numpy
matplotlib
seaborn
nltk
scikit-learn
xgboost
shap
dvc
```



## 📬 Contact

Project by [Dawit Neri](https://github.com/doffn) — powered by 💡 10 Academy.

```

