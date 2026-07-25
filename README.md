# 📊 E-Commerce Sales Prediction System

An **End-to-End Machine Learning Regression** project developed using **Python** to predict **E-commerce Sales Revenue** based on product information, customer purchase details, category, region, quantity, and purchase date. The project combines **Machine Learning**, **FastAPI**, and **Streamlit** to deliver a complete production-style sales prediction application with an interactive and user-friendly interface.

Designed as a real-world business analytics solution, this application demonstrates the complete machine learning lifecycle, including **data preprocessing**, **feature engineering**, **model training**, **model deployment**, and **web application development**. Users can instantly predict expected sales revenue through an intuitive interface while interacting with a trained regression model.

This project showcases practical experience in **Data Analytics**, **Machine Learning**, **REST API Development**, **Interactive Dashboard Design**, and **Full-Stack ML Deployment**, making it an excellent portfolio project for aspiring **Machine Learning Engineers**, **Data Scientists**, **Python Developers**, and **AI Engineers**.
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
