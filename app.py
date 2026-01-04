import streamlit as st
import pandas as pd
from market_engine import UdemyMarketEngine

# 1. Setup the Page
st.set_page_config(page_title="Udemy Strategy Optimizer", page_icon="🎓")
st.title("🎓 Course Success Predictor")
st.markdown("Enter your course details below to predict market performance.")

# 2. Load the Engine (Cached so it doesn't reload every click)
@st.cache_resource
def load_engine():
    engine = UdemyMarketEngine()
    engine.preprocess_and_train()
    return engine

try:
    engine = load_engine()
    st.success("AI Model Loaded Successfully!")
except Exception as e:
    st.error(f"Could not load data. Ensure 'udemy_courses.csv' is in the folder. Error: {e}")
    st.stop()

# 3. User Inputs
col1, col2 = st.columns(2)
with col1:
    title = st.text_input("Course Title", "The Complete Python Bootcamp")
    price = st.number_input("Price ($)", min_value=0.0, max_value=200.0, value=19.99)

with col2:
    subject = st.selectbox("Subject", ["Web Development", "Business Finance", "Musical Instruments", "Graphic Design"])
    level = st.selectbox("Level", ["All Levels", "Beginner Level", "Intermediate Level", "Expert Level"])

# 4. The Magic Button
if st.button("Predict Success"):
    # Use the programmatic API from market_engine
    result = engine.predict_course(title=title, price=price, subject=subject, level=level)
    
    # Display Results
    st.divider()
    st.metric(label="Predicted Subscribers", value=f"{result['prediction_int']:,}")
    st.metric(label="Market Performance", value=f"{result['percentile']:.1f}% of average")
    
    # Logic for Advice (Visualized)
    if result['prediction'] > 5000:
        st.balloons()
        st.success("🌟 This looks like a Best Seller!")
    elif result['prediction'] < 1000:
        st.warning("⚠️ Low Reach Expected.")
    
    # Display advice messages
    if result['advice']:
        st.subheader("💡 Strategic Recommendations")
        for msg in result['advice']:
            st.info(msg)
