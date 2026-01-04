import warnings

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
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
        print("[Train] Done. Ready for predictions.\n")

    def analyze_user_idea(self, title, price, subject, level):
        print(f"[Analyze] Course: '{title}'...")

        # Vectorize title
        title_vec = self.vectorizer.transform([title]).toarray()
        title_df = pd.DataFrame(title_vec, columns=[f"txt_{i}" for i in range(100)])

        # Encode inputs
        try:
            subj_enc = self.le_subject.transform([subject])[0]
            lvl_enc = self.le_level.transform([level])[0]
        except ValueError:
            print("[Warn] Unknown subject or level. Using defaults.")
            subj_enc = 0
            lvl_enc = 0

        input_data = pd.DataFrame({
            "price": [price],
            "subject_enc": [subj_enc],
            "level_enc": [lvl_enc],
        })

        final_input = pd.concat([input_data, title_df], axis=1)

        prediction = self.model.predict(final_input)[0]
        avg_subs = self.df["num_subscribers"].mean()
        percentile = (prediction / avg_subs) * 100 if avg_subs else 0.0

        print("\n" + "=" * 40)
        print(f"Results for: {title}")
        print("=" * 40)
        print(f"Predicted Subscribers: {int(prediction):,}")
        print(f"Market Performance:    {percentile:.1f}% of the average course")

        self._give_advice(prediction, price, title)

    def _give_advice(self, prediction, price, title):
        print("\nAdvice:")

        # Pricing advice
        if price > 50 and prediction < 1000:
            print(" - Price alert: This looks overpriced for expected reach. Try 19.99 or Free to build audience.")
        elif price == 0:
            print(" - Growth mode: Free courses pull more traffic; have an upsell plan.")

        # Title keyword advice
        power_words = ["Bootcamp", "Complete", "Master", "Guide", "Beginner"]
        if not any(word.lower() in title.lower() for word in power_words):
            print(f" - Title optimization: Try adding one of {power_words}.")

        # Validation
        if prediction > 5000:
            print(" - Winner: This setup resembles a best seller.")
        else:
            print(" - Risk: Expect competition or lower demand; iterate on title/price/positioning.")


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
