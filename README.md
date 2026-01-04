# 🎓 Udemy Market Strategy Engine

> **Transform guesswork into data-driven course strategy.**  
> An AI-powered platform that predicts Udemy course success and provides actionable optimization advice using historical market data.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/sklearn-ML-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 What This Does

This project converts a **static Udemy dataset** into an **interactive strategy consultant** for course creators. Instead of guessing what works, instructors get:

- **📊 Predictive Analytics**: ML model forecasts subscriber counts based on title, price, subject, and level
- **💡 Smart Recommendations**: NLP-powered advice on title optimization, pricing strategy, and market positioning
- **🎨 Interactive Dashboard**: Streamlit web app for instant predictions (no coding required)
- **📈 Market Insights**: Automated EDA with correlation heatmaps, distribution plots, and trend analysis

**Key Innovation**: Uses **TF-IDF vectorization** on course titles to extract "power keywords" (e.g., "Bootcamp", "Complete") that historically drive enrollment.

---

## 🏗️ Architecture

```
udemy-analysis/
├── app.py                  # Streamlit web interface (Phase 2)
├── market_engine.py        # Oracle ML model + optimization logic (Phase 1)
├── udemy_analysis.py       # Batch EDA pipeline with plots
├── udemy_courses.csv       # Kaggle dataset (3.6k+ courses)
├── requirements.txt        # Dependencies
├── .streamlit/config.toml  # Custom theming
└── outputs/                # Generated visualizations
```

**Tech Stack**:
- **ML**: Random Forest Regressor (scikit-learn) with 100 TF-IDF features
- **NLP**: Title keyword extraction via TfidfVectorizer
- **Web**: Streamlit for interactive deployment
- **Viz**: Seaborn + Matplotlib for exploratory plots

---

## 📦 Installation

### Prerequisites
- Python 3.10+ (tested with 3.14 beta)
- Kaggle account for dataset access

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/vihaankulkarni29/udemy-analysis.git
   cd udemy-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset** (via kagglehub)
   
   First, get your Kaggle API token:
   - Go to [Kaggle → Account → "Create New API Token"](https://www.kaggle.com/settings)
   - Set environment variables:
     ```bash
     # Windows
     set KAGGLE_USERNAME=your_username
     set KAGGLE_KEY=your_api_key
     
     # Linux/Mac
     export KAGGLE_USERNAME=your_username
     export KAGGLE_KEY=your_api_key
     ```
   
   Then download:
   ```python
   import kagglehub
   path = kagglehub.dataset_download("andrewmvd/udemy-courses")
   print("Path:", path)
   ```
   
   Copy `udemy_courses.csv` to the project root.

---

## 🎯 Usage

### Option 1: Web Interface (Recommended)

Launch the Streamlit app:
```bash
streamlit run app.py
```

Visit `http://localhost:8501` and:
1. Enter your course title (e.g., "The Complete Python Bootcamp")
2. Set price, subject, and level
3. Click **"Predict Success"** → Get instant forecasts + advice

**Example Output**:
```
Predicted Subscribers: 12,450
Market Performance: 389% of average
🌟 This looks like a Best Seller!
💡 Recommendations:
  - Growth mode: Free pulls more traffic; ensure an upsell plan.
  - Winner: resembles a best seller.
```

### Option 2: CLI Mode

Run the interactive terminal version:
```bash
python market_engine.py
```

Follow prompts to input course details and receive predictions.

### Option 3: Batch Analysis

Generate visualizations and summary stats:
```bash
python udemy_analysis.py
```

Outputs saved to `outputs/`:
- `subject_counts.png` - Course distribution by category
- `price_distribution.png` - Pricing trends
- `correlation_heatmap.png` - Feature relationships
- `reviews_vs_subscribers.png` - Engagement patterns

---

## 📊 Model Performance

**Oracle Engine (market_engine.py)**:
- Algorithm: Random Forest (100 estimators)
- Features: Price, Subject, Level + 100 TF-IDF title keywords
- Metrics: MAE ~3,370 | R² -0.05 (baseline on raw data)

**Full Pipeline (udemy_analysis.py)**:
- Algorithm: Random Forest (200 estimators) with preprocessing pipeline
- Features: Engineered (year, month, reviews_per_sub) + one-hot encoded categories
- Metrics: MAE ~375 | R² 0.92 (on hold-out set)

*Note: The Oracle model prioritizes interpretability for user-facing advice; the analysis pipeline maximizes accuracy.*

---

## 🎨 Deployment

### Streamlit Community Cloud (Free)

1. Push your code to GitHub (already done ✓)
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click **"New app"** → Select this repo → Set main file: `app.py`
4. Add `udemy_courses.csv` via **Secrets** (or upload to repo if public domain)
5. Deploy → Share the URL 🚀

### Local Network Access

Run with network visibility:
```bash
streamlit run app.py --server.address 0.0.0.0
```

Access from other devices: `http://<your-local-ip>:8501`

### Docker (Optional)

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

---

## 🧠 How It Works

### Phase 1: The Oracle Model (`market_engine.py`)

1. **Text Engineering**: Extracts keywords from 3.6k course titles using TF-IDF
2. **Feature Encoding**: Converts subjects/levels to numeric representations
3. **Prediction**: Random Forest estimates subscriber count
4. **Optimization Logic**: Compares prediction against market averages and suggests:
   - Price adjustments (if overpriced for expected reach)
   - Title improvements (missing "power words")
   - Risk assessment (competition/demand signals)

### Phase 2: Web Interface (`app.py`)

- **Caching**: `@st.cache_resource` prevents retraining on every interaction
- **Reactive UI**: Real-time predictions with visual feedback (balloons for winners!)
- **Advice Engine**: Displays strategic recommendations in digestible format

---

## 📚 Example Use Cases

| Scenario | Input | Prediction | Advice |
|----------|-------|------------|--------|
| **Generic Title** | "Learning Java", $100, Web Dev | 661 subs (20%) | Lower price to $19.99, add "Bootcamp" to title |
| **Optimized** | "Complete Java Bootcamp 2024", Free, Web Dev | 12,000+ subs (380%) | Winner! Ensure upsell strategy for free course |
| **Niche Market** | "Piano Basics", $25, Musical Instruments | 1,200 subs (37%) | Competitive space, test lower price or "Beginner Guide" |

---

## 🛠️ Advanced Features

### Programmatic API

Call predictions from other Python scripts:
```python
from market_engine import UdemyMarketEngine

engine = UdemyMarketEngine()
engine.preprocess_and_train()

result = engine.predict_course(
    title="Advanced React Patterns",
    price=49.99,
    subject="Web Development",
    level="Expert Level"
)

print(f"Predicted subs: {result['prediction_int']}")
print(f"Advice: {result['advice']}")
```

### Custom Analysis

Modify `udemy_analysis.py` to:
- Add new features (e.g., `num_lectures`, `content_duration`)
- Test XGBoost/LightGBM models
- Implement hyperparameter tuning with GridSearchCV

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] Add multi-class classification (predict "Best Seller" tier)
- [ ] Implement A/B testing simulator for title variations
- [ ] Integrate SHAP values for prediction explainability
- [ ] Build API endpoint (FastAPI) for third-party integrations

**To contribute**:
1. Fork the repo
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 Dataset

**Source**: [Udemy Courses Dataset](https://www.kaggle.com/datasets/andrewmvd/udemy-courses) (Kaggle)  
**Size**: 3,678 courses across 4 subjects  
**Features**: Title, Price, Subscribers, Reviews, Level, Subject, Published Date

**Citation**:
```
@dataset{udemy_courses_2021,
  author = {Andrew Maranhão},
  title = {Udemy Courses Dataset},
  year = {2021},
  publisher = {Kaggle},
  url = {https://www.kaggle.com/datasets/andrewmvd/udemy-courses}
}
```

---

## 📞 Contact

**Author**: Vihaan Kulkarni  
**GitHub**: [@vihaankulkarni29](https://github.com/vihaankulkarni29)  
**Project**: [udemy-analysis](https://github.com/vihaankulkarni29/udemy-analysis)

---

## 📜 License

MIT License - feel free to use for commercial/educational purposes.

---

## 🙏 Acknowledgments

- Kaggle community for the dataset
- scikit-learn team for ML tools
- Streamlit for making data apps accessible
- Course creators who inspire this work

---

**⭐ If this helps your course strategy, star the repo!**
