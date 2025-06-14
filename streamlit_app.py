import pickle
import os
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Parkinson's Disease Screening Tool", layout="centered")

# ---------------- VISITOR COUNTER ----------------
counter_file = "visitor_data.pkl"

# Load or initialize visitor data
if os.path.exists(counter_file):
    with open(counter_file, 'rb') as f:
        visitor_data = pickle.load(f)
else:
    visitor_data = {
        'count': 0,
        'timestamps': []
    }

if 'counted' not in st.session_state:
    st.session_state['counted'] = True
    visitor_data['count'] += 1
    visitor_data['timestamps'].append(str(datetime.datetime.now()))
    with open(counter_file, 'wb') as f:
        pickle.dump(visitor_data, f)

# ---------------- LOAD MODEL ----------------
parkinsons_model = pickle.load(open("parkinsons_model.sav", 'rb'))

# ---------------- SIDEBAR MENU ----------------
with st.sidebar:
    selected = option_menu("Main Menu", 
                           ["Welcome", "Prediction", "Analytics"], 
                           icons=['house', 'activity', 'bar-chart'],
                           menu_icon="cast", default_index=0)

# ---------------- WELCOME PAGE ----------------
if selected == "Welcome":
    st.markdown("<h1 style='text-align: center; color: green;'>🧠 Parkinson's Disease Screening App</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif", use_column_width=True)

    st.success(f"🌟 **Total Visitors:** {visitor_data['count']}")

    st.write("""
    **This tool helps in identifying early signs of Parkinson's Disease based on biomedical voice features.**

    ✅ AI-Powered Risk Estimation  
    ✅ Designed for Remote Settings  
    ✅ Empowers Clinical Decision-Making

    👉 Use the sidebar to get started!
    """)

# ---------------- PREDICTION PAGE ----------------
elif selected == "Prediction":
    st.markdown("<h2 style='text-align: center;'>🎙️ Parkinson's Disease Prediction</h2>", unsafe_allow_html=True)
    st.write("Fill in the biomedical voice features below:")

    with st.form("prediction_form"):
        jitter = st.number_input("Jitter (%)", min_value=0.0, format="%.5f")
        shimmer = st.number_input("Shimmer (dB)", min_value=0.0, format="%.5f")
        fo = st.number_input("Average Fundamental Frequency (Hz)", min_value=0.0)
        hnr = st.number_input("Harmonics-to-Noise Ratio (HNR)", min_value=0.0)
        spread1 = st.number_input("Spread1", min_value=-10.0, max_value=0.0, format="%.5f")
        spread2 = st.number_input("Spread2", min_value=0.0, format="%.5f")
        d2 = st.number_input("D2", min_value=0.0, format="%.5f")
        rpde = st.number_input("Recurrence Period Density Entropy (RPDE)", min_value=0.0, max_value=1.0, format="%.5f")
        DFA = st.number_input("Detrended Fluctuation Analysis (DFA)", min_value=0.0, max_value=2.0, format="%.5f")

        submitted = st.form_submit_button("Predict Parkinson's Disease")

    if submitted:
        input_data = [fo, jitter, shimmer, hnr, rpde, DFA, spread1, spread2, d2]
        input_array = np.array(input_data).reshape(1, -1)
        prediction = parkinsons_model.predict(input_array)[0]
        probability = parkinsons_model.predict_proba(input_array)[0][1] * 100

        if prediction == 1:
            st.error(f"🚨 The person is **likely** to have Parkinson's Disease.\n\n🧠 Prediction Confidence: {probability:.2f}%")
        else:
            st.success(f"✅ The person is **unlikely** to have Parkinson's Disease.\n\n🧠 Prediction Confidence: {probability:.2f}%")

# ---------------- ANALYTICS PAGE ----------------
elif selected == "Analytics":
    st.markdown("<h2 style='text-align: center;'>📊 Visitor Analytics</h2>", unsafe_allow_html=True)

    st.info(f"🧑‍💻 **Total Visitors:** {visitor_data['count']}")

    if len(visitor_data['timestamps']) > 0:
        st.write("### 🕒 **Visitor Log (Timestamps):**")
        st.dataframe(visitor_data['timestamps'])

    if st.button("🔄 Reset Visitor Counter"):
        visitor_data = {'count': 0, 'timestamps': []}
        with open(counter_file, 'wb') as f:
            pickle.dump(visitor_data, f)
        st.success("Visitor counter has been reset. Please refresh to see the update.")

    st.write("⚠️ **Note:** This data is stored locally in `visitor_data.pkl`. No external tracking is used.")
