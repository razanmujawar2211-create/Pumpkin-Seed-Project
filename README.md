
# 🎃 Pumpkin Seed Classification using Machine Learning

An end-to-end Machine Learning project that classifies pumpkin seeds based on their physical and geometric features.
The best performing model (Random Forest) is deployed using **FastAPI** with a clean **HTML user interface** for real-time predictions.

---

## 📌 Project Overview

This project demonstrates a complete ML workflow:

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Multiple model training and comparison
* Best model selection
* Model serialization
* Web deployment using FastAPI

The system allows users to input seed features and instantly get the predicted seed category.

---

## 🚀 Features

* ✅ Outlier removal using IQR
* ✅ Feature scaling with MinMaxScaler
* ✅ Exploratory Data Analysis with visualizations
* ✅ Multiple ML model comparison
* ✅ Random Forest selected as best model
* ✅ Model saved using Pickle
* ✅ FastAPI backend
* ✅ Responsive HTML frontend
* ✅ Real-time prediction

---

## 🧠 Machine Learning Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier ⭐ (Best)
* Multinomial Naive Bayes
* Support Vector Classifier
* Gradient Boosting Classifier

---

## 🏗️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Matplotlib, Seaborn**
* **FastAPI**
* **Jinja2**
* **HTML/CSS**
* **Uvicorn**

---

## 📂 Project Structure

```
Pumpkin-Seed-Classification/
│
├── app.py
├── model.pkl
├── Pumpkin_Seeds_Dataset.xlsx
├── pumpkin.ipynb
└── templates/
    └── index.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd Pumpkin-Seed-Classification
```

### 2️⃣ Install dependencies

```bash
pip install fastapi uvicorn jinja2 scikit-learn pandas numpy python-multipart
```

### 3️⃣ Run the application

```bash
uvicorn app:app --reload
```

### 4️⃣ Open in browser

```
http://127.0.0.1:8000
```

---

## 🧪 Example Input

Use these sample values in the UI:

| Feature           | Value    |
| ----------------- | -------- |
| Area              | 0.410519 |
| Perimeter         | 0.340661 |
| Major Axis Length | 0.294143 |
| Solidity          | 0.9916   |
| Extent            | 0.7151   |
| Roundness         | 0.8440   |
| Aspect Ration     | 1.7811   |
| Compactness       | 0.7487   |

---

## 🎯 Future Improvements

* 🔹 Hyperparameter tuning
* 🔹 Cross-validation
* 🔹 Sklearn pipeline automation
* 🔹 Docker containerization
* 🔹 Cloud deployment
* 🔹 Model monitoring

---

## 👤 Author

**Razan Mujawar**

---

⭐ If you found this project useful, feel free to star the repository!
