import warnings
from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

warnings.filterwarnings("ignore", category=FutureWarning)
sns.set(style="whitegrid", palette="crest")

DATA_FILE = "udemy_courses.csv"
OUTPUT_DIR = Path("outputs")


def load_data(data_file: str = DATA_FILE) -> pd.DataFrame:
    """Load the Udemy dataset, with a small fallback sample if missing."""
    try:
        df = pd.read_csv(data_file)
        print(f"Loaded dataset from {data_file} with shape {df.shape}")
    except FileNotFoundError:
        print(f"Dataset {data_file} not found; using small fallback sample.")
        sample = {
            "course_title": [
                "Python 101",
                "Finance for Beginners",
                "Web Dev Pro",
                "Piano Masterclass",
            ],
            "is_paid": [True, False, True, True],
            "price": [19.99, 0.0, 99.99, 19.99],
            "num_subscribers": [1000, 5000, 200, 150],
            "num_reviews": [50, 200, 20, 10],
            "level": [
                "Beginner Level",
                "All Levels",
                "Expert Level",
                "Beginner Level",
            ],
            "subject": [
                "Web Development",
                "Business Finance",
                "Web Development",
                "Musical Instruments",
            ],
            "published_timestamp": [
                "2017-01-15",
                "2016-05-20",
                "2017-10-10",
                "2015-02-28",
            ],
        }
        df = pd.DataFrame(sample)
    return df


def basic_inspection(df: pd.DataFrame) -> pd.DataFrame:
    print("\n--- TEMPO 1: BASICS ---")
    print("First 5 rows:\n", df.head())
    print("\nDataset Info:")
    print(df.info())
    print(f"\nShape before dropping duplicates: {df.shape}")
    df = df.drop_duplicates()
    print(f"Shape after dropping duplicates: {df.shape}")
    print("\nMissing Values per column:\n", df.isnull().sum())
    return df


def clean_and_cast(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["published_timestamp"] = pd.to_datetime(df["published_timestamp"], errors="coerce")
    df["is_paid"] = df["is_paid"].astype("bool", errors="ignore")
    # Coerce prices to numeric in case the column is read as text
    df["price"] = pd.to_numeric(df.get("price"), errors="coerce")
    # Fill simple numeric gaps so plots/modeling do not break
    for col in ["price", "num_subscribers", "num_reviews"]:
        if col in df:
            df[col] = df[col].fillna(df[col].median())
    # Fill text gaps with a placeholder
    for col in ["level", "subject", "course_title", "url"]:
        if col in df:
            df[col] = df[col].fillna("Unknown")
    # Convert is_paid to int for modeling stability
    if "is_paid" in df:
        df["is_paid"] = df["is_paid"].astype(int)
    # Drop rows with missing timestamps after coercion
    df = df.dropna(subset=["published_timestamp"])
    return df


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["year"] = df["published_timestamp"].dt.year
    df["month"] = df["published_timestamp"].dt.month
    df["reviews_per_sub"] = np.where(
        df["num_subscribers"] > 0,
        df["num_reviews"] / df["num_subscribers"],
        0.0,
    )
    df["log_subscribers"] = np.log(df["num_subscribers"] + 1)
    return df


def save_plot(fig: plt.Figure, name: str) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / name
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved figure -> {path}")


def plot_subject_counts(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(x="subject", data=df, order=df["subject"].value_counts().index, ax=ax)
    ax.set_title("Number of Courses per Subject")
    ax.set_xlabel("Subject")
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=20)
    save_plot(fig, "subject_counts.png")


def plot_price_distribution(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df["price"], bins=40, kde=True, ax=ax)
    ax.set_title("Course Price Distribution")
    ax.set_xlabel("Price")
    save_plot(fig, "price_distribution.png")


def plot_corr(df: pd.DataFrame) -> None:
    numerical = df[["price", "num_subscribers", "num_reviews"]]
    corr = numerical.corr()
    print("\nCorrelation Matrix:\n", corr)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    save_plot(fig, "correlation_heatmap.png")


def plot_reviews_vs_subscribers(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="num_reviews",
        y="num_subscribers",
        hue="subject",
        alpha=0.7,
        ax=ax,
    )
    ax.set_title("Reviews vs Subscribers by Subject")
    save_plot(fig, "reviews_vs_subscribers.png")


def prepare_ml_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    target = "num_subscribers"
    drop_cols = ["course_title", "published_timestamp", "log_subscribers", "url"]
    drop_cols = [c for c in drop_cols if c in df.columns]
    X = df.drop(columns=drop_cols + [target])
    y = df[target]
    return X, y


def build_pipeline(X: pd.DataFrame) -> Pipeline:
    categorical_cols = X.select_dtypes(include=["object", "bool"]).columns.tolist()
    numeric_cols = X.select_dtypes(exclude=["object", "bool"]).columns.tolist()

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical", categorical_transformer, categorical_cols),
            ("numeric", numeric_transformer, numeric_cols),
        ]
    )

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        n_jobs=-1,
    )

    pipe = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )
    return pipe


def train_and_evaluate(X: pd.DataFrame, y: pd.Series) -> None:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    pipe = build_pipeline(X)
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    print("\nModel performance on hold-out set:")
    print(f"MAE: {mae:0.2f}")
    print(f"R^2: {r2:0.3f}")


if __name__ == "__main__":
    df_raw = load_data()
    df_clean = basic_inspection(df_raw)
    df_clean = clean_and_cast(df_clean)

    print("\n--- TEMPO 2: INTERMEDIATE ---")
    print("\nCourses per Subject:\n", df_clean["subject"].value_counts())

    plot_subject_counts(df_clean)
    plot_price_distribution(df_clean)
    plot_corr(df_clean)
    plot_reviews_vs_subscribers(df_clean)

    print("\n--- TEMPO 3: COMPLEX ML PREP ---")
    df_features = add_features(df_clean)
    X, y = prepare_ml_data(df_features)
    print("Feature columns used for ML:", list(X.columns))
    train_and_evaluate(X, y)

    print("\nFinished. Plots saved to outputs/ directory.")
