# Phishing Email Detection using Machine Learning

## Project Overview
This project is a Flask-based web application that detects whether an email is **Phishing** or **Safe** using a Machine Learning model. The model is trained using email text data and classifies emails based on suspicious words, links, and textual patterns.

## Features
- Detects phishing emails from user input
- Classifies emails as **Phishing** or **Safe**
- Uses TF-IDF Vectorization for text feature extraction
- Trained using Logistic Regression
- Displays prediction result on a Flask web page
- Shows model accuracy and confusion matrix during training

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- HTML
- CSS
- Machine Learning

## Project Structure
```text
Phishing-email-check/
│
├── app.py
├── train_model.py
├── emails.csv
├── model.pkl
├── vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
