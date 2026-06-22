# SocialPulse: Twitter Sentiment Analyzer

### Research-Backed Twitter Sentiment Analysis using Supervised Machine Learning

## Overview

SocialPulse is a Machine Learning and Natural Language Processing (NLP) project developed to analyze sentiment in Twitter (X) posts and classify them as **Positive** or **Negative**.

The project is based on our research study:

**"Twitter Sentiment Analysis: A Benchmark Study of Supervised Machine Learning Approaches"**

The study evaluates and compares the performance of **8 supervised machine learning models** across two benchmark Twitter sentiment datasets: **Sentiment140** and **TweetEval**.

The project includes:

* End-to-end NLP preprocessing pipeline
* TF-IDF feature engineering
* Hyperparameter tuning using GridSearchCV
* Model benchmarking and comparison
* Performance visualization
* Interactive web application deployment

---

## Live Demo

🚀 **Try the application here**

https://huggingface.co/spaces/Shivangini2006/Tweet_Sentiment_Analyzer_ML

---

## Research Contribution

This project performs a controlled comparative benchmark study of classical Machine Learning techniques for Twitter sentiment classification.

### Datasets Used

#### Sentiment140

* 1.6 Million Tweets
* Binary Sentiment Classification
* Balanced subset of 100,000 tweets used

#### TweetEval

* Benchmark Twitter Sentiment Dataset
* Binary sentiment classification
* Class imbalance handled using SMOTE

---

## Machine Learning Models Evaluated

1. Logistic Regression
2. Naive Bayes
3. Linear SVM
4. K-Nearest Neighbors (KNN)
5. Decision Tree
6. Random Forest
7. XGBoost
8. Hard Voting Ensemble

---

## NLP Pipeline

### Text Preprocessing

* Lowercasing
* URL Removal
* Username Removal
* Emoji Removal
* Non-ASCII Character Removal
* Digit Removal
* Punctuation Removal
* Hashtag Normalization
* Repeated Character Normalization
* Tokenization
* Stopword Removal
* Lemmatization

### Feature Engineering

* TF-IDF Vectorization

### Data Balancing

* SMOTE (Synthetic Minority Oversampling Technique)

---

## Results

### Sentiment140 Dataset

| Model                | Accuracy   |
| -------------------- | ---------- |
| Logistic Regression  | **76.48%** |
| Hard Voting Ensemble | 76.22%     |
| Linear SVM           | 75.65%     |
| Naive Bayes          | 74.54%     |
| Random Forest        | 73.65%     |
| XGBoost              | 73.00%     |
| Decision Tree        | 69.93%     |
| KNN                  | 58.73%     |

### TweetEval Dataset

| Model                | Accuracy   |
| -------------------- | ---------- |
| Linear SVM           | **84.62%** |
| Hard Voting Ensemble | 84.40%     |
| Logistic Regression  | 84.06%     |
| Naive Bayes          | 82.07%     |
| Random Forest        | 79.59%     |
| XGBoost              | 79.57%     |
| Decision Tree        | 76.66%     |
| KNN                  | 41.61%     |

### Best Performing Models

| Dataset      | Best Model          | Accuracy   |
| ------------ | ------------------- | ---------- |
| Sentiment140 | Logistic Regression | **76.48%** |
| TweetEval    | Linear SVM          | **84.62%** |

### Key Findings

* Linear models consistently outperformed tree-based methods.
* Dataset quality had a greater impact than dataset size.
* Logistic Regression achieved the best performance on Sentiment140.
* Linear SVM achieved the best performance on TweetEval.
* Hard Voting Ensemble provided robust and consistent results across both datasets.

---

## Project Structure

```text
SocialPulse-Twitter_Sentiment_Analyzer/

├── Dataset/
├── Models/
├── Notebook/
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Shivangini-coder/SocialPulse-Twitter_Sentiment_Analyzer-ML_Resume.git
```

### Navigate to Project

```bash
cd SocialPulse-Twitter_Sentiment_Analyzer-ML_Resume
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Applications

* Brand Reputation Monitoring
* Customer Feedback Analysis
* Social Media Analytics
* Public Opinion Mining
* Market Research
* Political Sentiment Tracking

---

## Future Improvements

* BERT-based Sentiment Analysis
* RoBERTa Fine-Tuning
* Real-Time Twitter API Integration
* Multilingual Sentiment Analysis
* Aspect-Based Sentiment Analysis
* Deep Learning Architectures (LSTM, BiLSTM)

---

## Research Paper

**Twitter Sentiment Analysis: A Benchmark Study of Supervised Machine Learning Approaches**

Authors:

* Shivangini Gupta
* Shalu Kumari
* Dr. Ritu Rani
* Dr. Poonam Bansal
* Dr. Garima Jaiswal

---

## Author

### Shivangini Gupta

B.Tech (Computer Science & Artificial Intelligence)
Indira Gandhi Delhi Technical University for Women (IGDTUW)

LinkedIn:
[www.linkedin.com/in/shivangini-gupta-igdtuw](http://www.linkedin.com/in/shivangini-gupta-igdtuw)

GitHub:
https://github.com/Shivangini-coder

---

## Acknowledgements

This project was developed as part of a research study on benchmark evaluation of supervised machine learning models for Twitter sentiment analysis and aims to contribute toward reproducible and interpretable sentiment classification systems.

