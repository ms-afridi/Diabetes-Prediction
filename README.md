# 🩺 Diabetes Prediction Web App

A machine learning-powered web application that predicts the likelihood of diabetes in a patient based on diagnostic input features. Built with **Python**, **Flask**, and a **Logistic Regression** model trained on medical data.

---

## 📁 Project Structure

```
Diabetes-Prediction/
│
├── application.py           # Flask backend — routes and prediction logic
├── log_reg.pkl              # Trained Logistic Regression model
├── scalerr.pkl              # Fitted StandardScaler for input preprocessing
│
├── index.html               # Landing / home page
├── home.html                # Main input form page
├── single_prediction.html   # Result page showing prediction output
│
└── Cancer_Prediction.ipynb  # Jupyter notebook for model training & experimentation
                             # (also covers cancer prediction)
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed, then install the required packages:

```bash
pip install flask scikit-learn numpy pandas
```

### Running the App

```bash
python application.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. The user enters patient diagnostic data into the web form (e.g. glucose level, BMI, age, insulin, blood pressure, etc.).
2. The input is preprocessed using the saved **StandardScaler** (`scalerr.pkl`) to normalize the values.
3. The scaled input is passed to the **Logistic Regression** model (`log_reg.pkl`).
4. The app returns a prediction — either **Diabetic** or **Not Diabetic** — on the results page.

---

## 📊 Model

- **Algorithm:** Logistic Regression
- **Preprocessing:** Standard Scaling
- **Notebook:** `Cancer_Prediction.ipynb` contains the exploratory data analysis, model training, and evaluation steps.

---

## 🛠️ Tech Stack

| Layer       | Technology          |
|-------------|---------------------|
| Backend     | Python, Flask       |
| ML Model    | scikit-learn        |
| Frontend    | HTML                |
| Model Persistence | pickle (.pkl) |

---

## 📌 Notes

- The `.pkl` files are pre-trained and included in the repo, so no retraining is needed to run the app.
- The Jupyter notebook (`Cancer_Prediction.ipynb`) can be used to retrain or experiment with the model.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**ms-afridi** — [GitHub Profile](https://github.com/ms-afridi)
