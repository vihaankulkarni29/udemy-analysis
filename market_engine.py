import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings("ignore")


class UdemyMarketEngine:
    def __init__(self, data_path="udemy_courses.csv"):
        print("[Init] Loading data...")
        self.df = pd.read_csv(data_path)
        self.vectorizer = TfidfVectorizer(max_features=100, stop_words="english")
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.le_subject = LabelEncoder()
        self.le_level = LabelEncoder()

    def preprocess_and_train(self):
        print("[Train] Fitting Oracle model (title NLP + regression)...")

        # 1. Clean Data
        self.df = self.df.dropna()
        self.df = self.df.drop_duplicates()

        # 2. Text Engineering
        title_vectors = self.vectorizer.fit_transform(self.df["course_title"]).toarray()
        title_df = pd.DataFrame(title_vectors, columns=[f"txt_{i}" for i in range(100)])

        # 3. Categorical Encoding
        self.df["subject_enc"] = self.le_subject.fit_transform(self.df["subject"])
        self.df["level_enc"] = self.le_level.fit_transform(self.df["level"])

        # 4. Feature Assembly
        X_numerical = self.df[["price", "subject_enc", "level_enc"]].reset_index(drop=True)
        X = pd.concat([X_numerical, title_df], axis=1)
        y = self.df["num_subscribers"]

        # 5. Train
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2
        )
        self.model.fit(self.X_train, self.y_train)

        preds = self.model.predict(self.X_test)
        self.metrics_ = {
            "mae": float(mean_absolute_error(self.y_test, preds)),
            "r2": float(r2_score(self.y_test, preds)),
        }
        print(
            f"[Eval] MAE: {self.metrics_['mae']:.2f} | R^2: {self.metrics_['r2']:.3f}"
        )
        print("[Train] Done. Ready for predictions.\n")

    def analyze_user_idea(self, title, price, subject, level):
        print(f"[Analyze] Course: '{title}'...")
        result = self.predict_course(title=title, price=price, subject=subject, level=level)

        print("\n" + "=" * 40)
        print(f"Results for: {title}")
        print("=" * 40)
        print(f"Predicted Subscribers: {result['prediction_int']:,}")
        print(f"Market Performance:    {result['percentile']:.1f}% of the average course")

        self._print_advice(result["advice"])

    def predict_course(self, title, price, subject, level):
        """Programmatic prediction interface (no prints)."""
        final_input = self._prepare_input(title=title, price=price, subject=subject, level=level)

        prediction = float(self.model.predict(final_input)[0])
        avg_subs = self.df["num_subscribers"].mean()
        percentile = (prediction / avg_subs) * 100 if avg_subs else 0.0
        advice = self._advice_messages(prediction, price, title)

        return {
            "prediction": prediction,
            "prediction_int": int(prediction),
            "percentile": percentile,
            "advice": advice,
        }

    def _prepare_input(self, title, price, subject, level):
        # Vectorize title
        title_vec = self.vectorizer.transform([title]).toarray()
        title_df = pd.DataFrame(title_vec, columns=[f"txt_{i}" for i in range(100)])

        # Encode inputs with fallbacks
        try:
            subj_enc = int(self.le_subject.transform([subject])[0])
        except ValueError:
            print("[Warn] Unknown subject; defaulting to first known subject.")
            subj_enc = 0

        try:
            lvl_enc = int(self.le_level.transform([level])[0])
        except ValueError:
            print("[Warn] Unknown level; defaulting to first known level.")
            lvl_enc = 0

        input_data = pd.DataFrame(
            {
                "price": [price],
                "subject_enc": [subj_enc],
                "level_enc": [lvl_enc],
            }
        )

        return pd.concat([input_data, title_df], axis=1)

    def _advice_messages(self, prediction, price, title):
        advice = []

        if price > 50 and prediction < 1000:
            advice.append(
                "Price alert: Overpriced for expected reach. Try 19.99 or Free to build audience."
            )
        elif price == 0:
            advice.append("Growth mode: Free pulls more traffic; ensure an upsell plan.")

        power_words = ["Bootcamp", "Complete", "Master", "Guide", "Beginner"]
        if not any(word.lower() in title.lower() for word in power_words):
            advice.append(f"Title optimization: add one of {power_words}.")

        if prediction > 5000:
            advice.append("Winner: resembles a best seller.")
        else:
            advice.append("Risk: competition or low demand; iterate on title/price/positioning.")

        return advice

    def _print_advice(self, advice):
        print("\nAdvice:")
        for msg in advice:
            print(f" - {msg}")


if __name__ == "__main__":
    engine = UdemyMarketEngine()
    engine.preprocess_and_train()

    print("Udemy Course Strategy Tool")
    print("Subjects: Business Finance, Graphic Design, Musical Instruments, Web Development")
    print("Levels: All Levels, Beginner Level, Expert Level, Intermediate Level")
    print("-" * 30)

    while True:
        t = input("\nEnter Course Title (or 'q' to quit): ")
        if t.lower() == "q":
            break

        try:
            p = float(input("Enter Price (0 for Free): "))
            s = input("Enter Subject: ")
            l = input("Enter Level: ")

            engine.analyze_user_idea(title=t, price=p, subject=s, level=l)
        except Exception as e:
            print(f"Error: {e}. Please try again.")
