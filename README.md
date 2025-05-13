# 🛡️ PhishGuard Lite: Simple Phishing URL Detector

PhishGuard Lite is a lightweight machine learning-based tool that detects phishing websites using basic URL features. Built with simplicity and efficiency in mind, it's ideal for educational purposes or as a starting point for more advanced cybersecurity models.

---

## 📌 Project Overview

Phishing attacks trick users into giving up sensitive information via deceptive websites. This project uses a dataset of URLs and their associated features to train a Naive Bayes model that classifies them as either **Safe** or **Phishing**.

---

## Project Structure

PhishGuard-Lite/
├── data/ # Contains phishing dataset (CSV)
├── notebooks/ # Jupyter/Colab notebook
├── src/ # Python modules (helpers, feature engineering, modeling)
│ ├── utils.py # Helper functions (data loading, missing handling)
│ ├── features.py # Feature engineering logic
│ └── model.py # Model training and evaluation
├── phishing.csv # Processed dataset (optional)
└── README.md # Project description and instructions

---

## Features

- Handles missing values and performs basic data preprocessing.
- Visualizes label distribution and confusion matrix.
- Uses **Gaussian Naive Bayes** for classification.
- Evaluates model using accuracy, precision, recall, and F1-score.
- Clean modular codebase with reusable utility functions.

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib
- Google Colab

---

## Dataset

- Source: [Kaggle - Phishing Dataset URL](https://www.kaggle.com/datasets/lilly1739/phishing-dataset-url)
- Features include:
  - `haveDash`
  - `domainLen`
  - `is@`
  - `isredirect`
  - and more...

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/irmakkoseoglu/PhishGuard-Lite.git
   cd PhishGuard-Lite
   
2. (Optional) Open the Colab notebook from the notebooks/ directory.

3. Install required libraries:
   pip install -r requirements.txt
   
4. Run model.py or step through the notebook to see the results.

🎯 Example Results
Accuracy: ~88%

Precision: ~90%

Recall: ~86%

Note: Results may vary depending on data split and preprocessing.

✨ Future Improvements
Include more complex models (e.g., Random Forest, XGBoost)

Add URL-based NLP features

Deploy as a simple web app

👩‍💻 Author
İrmak Köseoğlu
Feel free to reach out on LinkedIn or open issues for questions & feedback.

📝 License
This project is licensed under the MIT License.
