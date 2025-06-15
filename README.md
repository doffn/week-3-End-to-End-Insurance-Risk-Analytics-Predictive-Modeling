
# 📊 Week 3 Project: End-to-End Insurance Risk Analytics & Predictive Modeling

## 📝 Overview

This project aims to build an end-to-end pipeline for analyzing insurance risk based on customer, vehicle, and claims data. The first phase (Task 1) focuses on exploratory data analysis (EDA), risk metric engineering, and identifying insights from patterns in premium and claims behavior.

---

## 🏗️ Project Structure

```

.
├── .vscode/                   # Editor settings (optional)
├── .github/workflows/        # CI/CD pipelines (GitHub Actions)
│   └── unittests.yml
├── src/                      # Source code modules
│   └── **init**.py
├── notebooks/                # Jupyter notebooks
│   └── Task1.ipynb           # Main EDA notebook
├── scripts/                  # Helper scripts (e.g., data loaders, utilities)
├── tests/                    # Unit tests
│   └── **init**.py
├── .gitignore                # Files to ignore in version control
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies

````

---

## ⚙️ Setup Instructions

### 🧪 1. Clone the Repository

```bash
git clone https://github.com/doffn/week-3-End-to-End-Insurance-Risk-Analytics-Predictive-Modeling.git
cd insurance-risk-analytics-task1
````

### 🐍 2. Create & Activate Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:

* `pandas`, `numpy` – data handling
* `matplotlib`, `seaborn` – visualizations
* `nltk` – natural language preprocessing (future use)
* `dvc` – data version control

---

## 📈 Key Analysis Tasks (in `notebooks/Task1.ipynb`)

### ✅ Data Loading & Summary

* Converted pipe-delimited `.txt` data into `.csv`
* Used pandas to inspect structure (`df.info()`, `df.describe()`)

### 🔍 Feature Exploration

* Visualized `TotalPremium`, `TotalClaims` with histograms and boxplots
* Evaluated missing data
* Examined categorical features like `Province`, `Gender`, and `VehicleType`

### 📊 Risk Metric Engineering

* Calculated `Loss Ratio`, `Claim Frequency`, and `Claim Severity`

```python
df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
df['LossRatio'].replace([np.inf, -np.inf], np.nan, inplace=True)

claim_frequency = (df['TotalClaims'] > 0).mean()
```

### 🔁 Grouped Insights

* Aggregated loss ratios by `Province`, `VehicleType`, and `Gender`
* Temporal trends plotted by `TransactionMonth`

```python
monthly = df.groupby('TransactionMonth')[['TotalPremium', 'TotalClaims']].sum()
monthly.plot()
```

### 🧪 Correlations & Outliers

* Heatmap of numeric feature correlations
* Used log-scale scatter plots and boxplots to examine extreme values

---

## 🚦 CI/CD: GitHub Actions

This project includes a GitHub Actions workflow to:

* Install dependencies
* Run automated unit tests via `pytest`

Workflow: `.github/workflows/unittests.yml`

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
- name: Run tests
  run: |
    pytest
```

---

## 🔄 Data Versioning

To track data versions and workflows:

```bash
dvc init
dvc add data/MachineLearningRating_v3.csv
git add data/MachineLearningRating_v3.csv.dvc .gitignore
git commit -m "Track dataset with DVC"
```

---

## 🚀 Next Steps

* Handle missing values and normalize skewed distributions
* Feature engineering for supervised modeling
* Develop predictive models to classify and forecast insurance risk

---

## 🧪 Testing

All unit tests are placed under the `tests/` folder. Run:

```bash
pytest
```

---

## 👤 Author

**Dawit Neri**
**www.doffneri.vercel.app**

---

## 📜 License

This project is for week 3 interim submission and research purposes only.

```

