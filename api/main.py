from fastapi import FastAPI
from pydantic import BaseModel
import os
import joblib  # ✅ use joblib, 

from src.issue_classifier import detect_issue_category
from src.priority_logic import assign_priority, recommend_action
from src.feature_engineering import preprocess_text  # ONLY preprocessing

app = FastAPI(
    title="Customer Feedback Analyzer",
    version="1.0"
)


class FeedbackRequest(BaseModel):
    feedback: str

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")

# ---------------- LOAD ARTIFACTS ----------------
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# ---------------- ROUTES ----------------
@app.get("/")
def home():
    return {"message": "Customer Feedback API is running"}

@app.post("/analyze")
def analyze_feedback(request: FeedbackRequest):
    feedback = request.feedback

    clean_text = preprocess_text(feedback)
    vectorized_text = vectorizer.transform([clean_text])

    sentiment = model.predict(vectorized_text)[0]

    issue = detect_issue_category(feedback)
    priority = assign_priority(sentiment, issue)
    action = recommend_action(priority)

    return {
        "feedback": feedback,
        "sentiment": sentiment,
        "issue_category": issue,
        "priority": priority,
        "recommended_action": action
    }
