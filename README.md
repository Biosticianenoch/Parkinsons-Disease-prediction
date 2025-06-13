# 🧠 Parkinson's Disease Detection Web App

---

## 🎯 Overview

Welcome to the **Parkinson's Disease Detection Web App**, an AI-powered platform designed to predict the likelihood of Parkinson's Disease using voice measurements. This project leverages machine learning and an intuitive **Streamlit-based UI** to help users perform quick assessments, receive recommendations, explore FAQs, view real-time analytics, and even support the project via donations.

---

## 🚀 Live Demo

🚧 *Deployment in progress...*

> You can also run it locally by following the setup instructions below.

---

## ✨ Key Features

✅ **ML-Powered Parkinson's Prediction**
✅ **Beautiful Sidebar Navigation**
✅ **Realtime Prediction Logging & Analytics**
✅ **Comprehensive FAQs Section**
✅ **Health & Lifestyle Recommendations**
✅ **Support & Donate Page (PayPal, Mpesa, Bank Transfer)**
✅ **Fully Responsive & Minimalist UI**

---

## 🖼️ Screenshots

| Home | Prediction | Analytics | Donate |
| ---- | ---------- | --------- | ------ |
|      |            |           |        |

---

## 🛠️ Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/parkinsons-detection-app.git
cd parkinsons-detection-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Add ML Model File

Place `parkinsons_model.sav` in this directory:

```
~/Downloads/parkinsons_model.sav
```

### 5. Launch the App

```bash
streamlit run app.py
```

---

## 📋 App Structure

```
📦 parkinsons-detection-app
│
├── app.py                  # Streamlit Main App
├── parkinsons_model.sav    # ML Model (Download directory)
├── prediction_logs.csv     # Auto-generated prediction logs
├── requirements.txt        # Required Python Packages
└── README.md               # This file
```

---

## 🔍 App Pages Description

| Page                 | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| **Welcome**          | Brief intro, app features, how-to instructions.             |
| **Prediction**       | Input 22 voice-related features for Parkinson's prediction. |
| **Recommendations**  | Health tips and care suggestions.                           |
| **FAQs**             | Educational info on Parkinson's & app usage.                |
| **Analytics**        | Live logs, charts, and prediction stats.                    |
| **Support & Donate** | Accepting donations via PayPal, Mpesa, Bank transfer.       |

---

## 📊 Example Analytics Output

```
Total Predictions Made: 50

Recent Predictions:
--------------------
Timestamp              Result
2025-06-13 10:23:45    Parkinson's Detected
2025-06-13 11:15:22    No Parkinson's
```

---

## 💖 How to Support

| Method            | Details                                                               |
| ----------------- | --------------------------------------------------------------------- |
| **PayPal**        | [dataquestsolutions2@gmail.com](mailto:dataquestsolutions2@gmail.com) |
| **Mpesa/MTN**     | +25401344230                                                          |
| **Bank Transfer** | KCB Bank, Account: 1340849054, Paybill: 522522                        |

---

## ⚠️ Disclaimer

> **Note:** This tool is an educational prototype and NOT a medical diagnostic device. Always consult a certified medical professional for health decisions.

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Enock Bereka**
📧 [enochosenwafulah@gmail.com](mailto:enochosenwafulah@gmail.com)

---

## ⭐ Contributions

Contributions, issues, and feature requests are welcome!

---

### 🚧 Future Plans

* 📱 Build a mobile-friendly version
* 🔔 Add email notifications for predictions

---

> *"Empowering early Parkinson's detection using AI & accessible technology."*
