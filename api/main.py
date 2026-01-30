from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import os
import joblib  # ✅ use joblib, 

from src.issue_classifier import detect_issue_category
from src.priority_logic import assign_priority, recommend_action
from src.feature_engineering import preprocess_text  # ONLY preprocessing

from src.database import get_db_connection  

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

    # Edge case 
    if not feedback.strip():
        return {"error": "Feedback text cannot be empty"}


    clean_text = preprocess_text(feedback)
    vectorized_text = vectorizer.transform([clean_text])

    # Predict sentiment
    sentiment = model.predict(vectorized_text)[0]

    # Predict confidence
    probs = model.predict_proba(vectorized_text)[0]
    confidence = round(max(probs), 2)


    issue = detect_issue_category(feedback)
    priority = assign_priority(sentiment, issue)
    action = recommend_action(priority)


#sql

    try:
            db = get_db_connection()
            cursor = db.cursor()

            query = """
            INSERT INTO feedback
            (feedback_text, sentiment, confidence, issue_category, priority, recommended_action)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            cursor.execute(query, (
                feedback,
                sentiment,
                confidence,
                issue,
                priority,
                action
            ))

            db.commit()
            cursor.close()
            db.close()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "feedback": feedback,
        "sentiment": sentiment,
        "confidence": confidence,
        "issue_category": issue,
        "priority": priority,
        "recommended_action": action
    }



# fetch data
@app.get("/feedbacks")
def get_feedbacks():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM feedback ORDER BY created_at DESC"
        )
        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))