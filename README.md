# e_commerce_sales_prediction
# 📊 E-commerce Sales Prediction App

A complete end-to-end Machine Learning project that predicts **E-commerce Sales** based on product details, category, region, quantity, and purchase date.

This project demonstrates the integration of **Machine Learning, FastAPI, and Streamlit deployment**, making it a practical full-stack ML application.

---

## 🚀 Live Demo
🔗 **Streamlit App:** [https://ecommercesalesprediction-tfy5kv33pv2cjbcutcmhcw.streamlit.app/]

🔗 **FastAPI Docs (Optional):** [http://127.0.0.1:8000/]

---

# 📌 Project Overview

This application predicts expected sales revenue for an e-commerce business using a trained Machine Learning model.

Users can:
- Select product type
- Choose category
- Select region
- Enter quantity
- Enter purchase date
- Get instant predicted sales output

The project includes:

✅ Machine Learning model training  
✅ Model serialization using Pickle (`.pkl`)  
✅ FastAPI backend API  
✅ Frontend integration with HTML/CSS/JavaScript  
✅ Streamlit deployment version  
✅ Input validation and interactive UI  

---

# 🛠 Tech Stack

## Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Regressor

## Backend
- FastAPI
- Uvicorn
- Pydantic
- Jinja2

## Frontend
- HTML
- CSS
- JavaScript

## Deployment
- Streamlit Cloud
- GitHub

---

# 📂 Project Structure

```bash
e_commerce_sales_prediction/
│
├── app.py                # FastAPI backend
├── streamlit_app.py      # Streamlit deployment app
├── sales_model.pkl       # Trained ML model
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
│
├── templates/
│   └── index.html        # FastAPI frontend UI
│
└── ecommerce_sales_data.csv
