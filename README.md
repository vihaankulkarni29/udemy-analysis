# Udemy Course Analysis

Lightweight pipeline to inspect the Kaggle Udemy Courses dataset, produce summary plots, and train a simple baseline model.

## Setup
1. Python 3.10+ recommended (repo tested with 3.14 beta env).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Get the data (via kagglehub)
1. Create a Kaggle API token (Kaggle > Account > "Create New API Token").
2. Set credentials in your shell:
   ```bash
   set KAGGLE_USERNAME=your_username
   set KAGGLE_KEY=your_api_token
   ```
3. Optional: keep the download here
   ```bash
   set KAGGLE_DATASET_CACHE_DIR=%CD%
   ```
4. Download:
   ```python
   import kagglehub
   path = kagglehub.dataset_download("andrewmvd/udemy-courses")
   print("Path to dataset files:", path)
   ```
5. Copy or point `udemy_analysis.py` to the `udemy_courses.csv` produced by kagglehub (default cache path is printed).

## Run
From the repo root:
```bash
python udemy_analysis.py
```

Outputs are written to `outputs/` (plots) and metrics are printed to stdout. The script ignores `.csv` and generated assets via `.gitignore`.
