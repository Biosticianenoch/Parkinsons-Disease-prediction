import pickle
import streamlit as st
import os
import numpy as np
import pandas as pd
from datetime import datetime
from streamlit_option_menu import option_menu

# ---- Load Model ---- #
parkinsons_model = pickle.load(open("parkinsons_model.sav", 'rb'))

# ---- CSV Log Setup ---- #
LOG_FILE = "prediction_logs.csv"

if not os.path.exists(LOG_FILE):
    df_log = pd.DataFrame(columns=["Timestamp", "Result"])
    df_log.to_csv(LOG_FILE, index=False)

def log_prediction(result):
    df_log = pd.read_csv(LOG_FILE)
    new_entry = pd.DataFrame({
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Result": [result]
    })
    df_log = pd.concat([df_log, new_entry], ignore_index=True)
    df_log.to_csv(LOG_FILE, index=False)

# ---- Sidebar Navigation ---- #
with st.sidebar:
    selected = option_menu(
        menu_title="Parkinson's App Menu",
        options=["Welcome", "Prediction", "Recommendations", "FAQs", "Analytics", "Support & Donate"],
        icons=["house", "activity", "lightbulb", "question-circle", "bar-chart", "credit-card"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )

# ---- Pages ---- #

# 1. Welcome Page
if selected == "Welcome":
    st.title("Welcome to the Parkinson's Disease Detection App")
    st.write("""
        This application predicts the likelihood of Parkinson's Disease based on biomedical voice measurements.
        
        *Features:*
        - Accurate Parkinson's Disease Prediction
        - Personalized Health Recommendations
        - Frequently Asked Questions (FAQs)
        - Real-Time Usage Analytics
        - Option to Support the Developer

        ➡ Use the sidebar to navigate to the *Prediction* page to get started!
    """)

# 2. Prediction Page
elif selected == "Prediction":
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        avg_fundamental_freq = st.number_input('Average vocal fundamental frequency (Hz)', value=0.0)
    with col2:
        max_fundamental_freq = st.number_input('Maximum vocal fundamental frequency (Hz)', value=0.0)
    with col3:
        min_fundamental_freq = st.number_input('Minimum vocal fundamental frequency (Hz)', value=0.0)
    with col4:
        jitter_percent = st.number_input('MDVP:Jitter (%)', value=0.0)
    with col5:
        jitter_abs = st.number_input('MDVP:Jitter (Abs)', value=0.0)

    with col1:
        rap = st.number_input('MDVP:RAP', value=0.0)
    with col2:
        ppq = st.number_input('MDVP:PPQ', value=0.0)
    with col3:
        ddp = st.number_input('Jitter:DDP', value=0.0)
    with col4:
        shimmer = st.number_input('MDVP:Shimmer', value=0.0)
    with col5:
        shimmer_db = st.number_input('MDVP:Shimmer (dB)', value=0.0)

    with col1:
        apq3 = st.number_input('Shimmer:APQ3', value=0.0)
    with col2:
        apq5 = st.number_input('Shimmer:APQ5', value=0.0)
    with col3:
        apq = st.number_input('MDVP:APQ', value=0.0)
    with col4:
        dda = st.number_input('Shimmer:DDA', value=0.0)
    with col5:
        nhr = st.number_input('Noise-to-Harmonics Ratio (NHR)', value=0.0)

    with col1:
        hnr = st.number_input('Harmonics-to-Noise Ratio (HNR)', value=0.0)
    with col2:
        rpde = st.number_input('Recurrence Period Density Entropy (RPDE)', value=0.0)
    with col3:
        dfa = st.number_input('Detrended Fluctuation Analysis (DFA)', value=0.0)
    with col4:
        spread1 = st.number_input('Spread1', value=0.0)
    with col5:
        spread2 = st.number_input('Spread2', value=0.0)

    with col1:
        d2 = st.number_input('D2 (Correlation Dimension)', value=0.0)
    with col2:
        ppe = st.number_input('Pitch Period Entropy (PPE)', value=0.0)

    if st.button("Get Parkinson's Test Result"):
        user_input = [
            avg_fundamental_freq, max_fundamental_freq, min_fundamental_freq,
            jitter_percent, jitter_abs, rap, ppq, ddp,
            shimmer, shimmer_db, apq3, apq5, apq, dda,
            nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe
        ]
        user_input = np.asarray(user_input).reshape(1, -1)
        prediction = parkinsons_model.predict(user_input)

        if prediction[0] == 1:
            diagnosis = "The person has Parkinson's disease"
            st.error(diagnosis)
        else:
            diagnosis = "The person does not have Parkinson's disease"
            st.success(diagnosis)

        log_prediction(diagnosis)

# 3. Recommendations Page
elif selected == "Recommendations":
    st.title("Health Recommendations")
    st.write("""
    Based on Parkinson's disease risk, here are some general health tips:

    - *Consult a Neurologist*: For clinical evaluation and further testing.
    - *Voice Therapy*: To improve speech difficulties associated with Parkinson's.
    - *Physical Exercise*: Engage in yoga, tai chi, or balance training.
    - *Nutritious Diet*: Eat fresh fruits, vegetables, and omega-3 fatty acids.
    - *Medication Adherence*: If prescribed by a healthcare provider.

    These recommendations are general. Always consult your doctor for personalized advice.
    """)

# 4. FAQs Page
elif selected == "FAQs":
    st.title("Frequently Asked Questions (FAQs)")

    with st.expander("❓ What is Parkinson's Disease?"):
        st.write("Parkinson's disease is a long-term degenerative disorder of the central nervous system affecting movement.")

    with st.expander("🤔 How accurate is this app?"):
        st.write("This app uses a machine learning model trained on biomedical data. It's not a substitute for professional medical diagnosis.")

    with st.expander("⚙ What data is used?"):
        st.write("The app uses 22 biomedical voice measurements including jitter, shimmer, fundamental frequencies, and entropy measures.")

    with st.expander("🏥 Should I rely solely on this result?"):
        st.write("No. This is a supportive tool — consult a certified neurologist for confirmation.")

# 5. Analytics Page
elif selected == "Analytics":
    st.title("App Usage Analytics")

    df_log = pd.read_csv(LOG_FILE)
    st.write("### Total Predictions Made:", len(df_log))

    st.write("### Recent Predictions:")
    st.dataframe(df_log.tail(10))

    result_counts = df_log["Result"].value_counts()
    st.write("### Prediction Summary:")
    st.bar_chart(result_counts)

    st.write("### Full Log Data:")
    st.dataframe(df_log)

# 6. Support & Donate Page
elif selected == "Support & Donate":
    st.title("Support & Donate 💖")
    st.write("""
    If you find this Parkinson's Detection App valuable, please consider supporting its development!

    Your contribution helps maintain and improve this free tool for everyone.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💳 Donate via PayPal")
        st.write("dataquestsolutions2@gmail.com")

    with col2:
        st.subheader("☕ Donate via Mpesa/MTN")
        st.write("+25401344230")

    st.subheader("💼 Bank Transfer Details")
    st.write("""
    - *Bank Name*: KCB Bank (Only for Kenyans)  
    - *Account Name*: DATAQUEST SOLUTIONS
    - *Paybill*: 522522
    - *Account Number*: 1340849054  
    - *SWIFT Code*: KCBLKENX
    """)

    st.subheader("📧 Contact for Support")
    st.write("Email: enochosenwafulah@gmail.com")
