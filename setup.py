import os

# Define folder and file structure
folders = [
    ".vscode",
    ".github/workflows",
    "src",
    "notebooks",
    "scripts",
    "tests"
]

files = {
    ".gitignore": "",
    "README.md": "# Week 3 Project: End-to-End Insurance Risk Analytics & Predictive Modeling\n",
    "requirements.txt": "\n".join([
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "nltk",
        "dvc",

    ]),
    ".github/workflows/unittests.yml": """name: Run Python tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.10
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
""",
    "src/__init__.py": "",
    "tests/__init__.py": "",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Project structure created successfully.")