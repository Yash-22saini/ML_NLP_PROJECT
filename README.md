# Customer Feedback Analysis System (NLP + ML + FastAPI)

An **industry-ready Customer Feedback Analysis API** that uses **Natural Language Processing (NLP)** and **Machine Learning** to analyze customer feedback, determine sentiment, classify issues, assign priority, recommend actions, and persist results in **MySQL**.

This project is designed as a **real-time inference service**, following clean architecture and production best practices.

---

## 🚀 Features

* Sentiment Analysis (Positive / Neutral / Negative)
* TF-IDF based text feature extraction
* Machine Learning model inference
* Issue category detection
* Priority assignment & action recommendation
* FastAPI REST API
* MySQL data storage & retrieval
* Environment variable based configuration (.env)
* Load & latency optimized API

---

## 🧱 Tech Stack

* **Language**: Python
* **NLP**: TF-IDF, text preprocessing
* **ML Models**: Logistic Regression, Random Forest
* **Backend**: FastAPI
* **Database**: MySQL
* **Deployment Server**: Uvicorn
* **Environment Management**: python-dotenv

---

## 📁 Project Structure

```
customer_project/
│
├── api/
│   └── main.py
│
├── src/
│   ├── db.py
│   ├── feature_engineering.py
│   ├── issue_classifier.py
│   ├── priority_logic.py
│   └── __init__.py
│
├── models/
│   ├── sentiment.pkl
│   └── tfidf_vectorizer.pkl
│
├── data/
│   └── feedback.csv
│
├── .env
├── requirements.txt
├── steps.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
uv venv
```

Activate the environment.

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in project root:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=customer_feedback
```

---

### 4️⃣ Create MySQL Database & Table

```sql
CREATE DATABASE customer_feedback;

USE customer_feedback;

CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    feedback_text TEXT,
    sentiment VARCHAR(50),
    confidence FLOAT,
    issue_category VARCHAR(100),
    priority VARCHAR(50),
    recommended_action VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ▶️ Running the API

```bash
uvicorn api.main:app --workers 4
```

API will run at:

```
http://127.0.0.1:8000
```

---

## 🔌 API Endpoints

### ✅ Health Check

```
GET /
```

Response:

```json
{"message": "Customer Feedback API is running"}
```

---

### 📩 Analyze Feedback

```
POST /analyze
```

Request:

```json
{
  "feedback": "The delivery was slow and support was unhelpful"
}
```

Response:

```json
{
  "feedback": "The delivery was slow and support was unhelpful",
  "sentiment": "negative",
  "confidence": 0.82,
  "issue_category": "service",
  "priority": "high",
  "recommended_action": "Immediate escalation"
}
```

---

### 📊 Fetch Stored Feedback

```
GET /feedbacks
```

Returns all stored feedback records from MySQL.

---

## ⚡ Performance & Scalability

* Model and vectorizer loaded at startup to reduce latency
* Multiple Uvicorn workers to handle concurrent requests
* Lightweight DB interactions per request
* Latency measured at API level

---

## 🧠 Design Decisions

* **TF-IDF** chosen for simplicity and explainability
* **FastAPI** for high-performance REST APIs
* **MySQL** for structured, persistent storage
* **Environment variables** for secure credential management
* **Single DB module** for clean separation of concerns

---

## 🔮 Future Enhancements

* JWT authentication
* API rate limiting
* Dashboard for feedback analytics
* Cloud deployment (AWS / Render)
* Advanced NLP models (BERT)

---

## 👤 Author

**Yash Saini**
Data Science | Machine Learning | NLP

---

## ✅ Project Status

**Production-ready ML API with database integration** 🚀
