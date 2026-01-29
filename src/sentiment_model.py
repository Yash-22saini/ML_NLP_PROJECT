import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from src.feature_engineering import get_tfidf_vectorizer, preprocess_text


def train_and_evaluate():
    # Load dataset
    df = pd.read_csv("data/feedback.csv")

    X = df["feedback_text"]
    y = df["sentiment"]

    # -------- CLEAN TEXT --------
    cleaned_texts = X.apply(preprocess_text)

    # -------- TF-IDF (TRAINING) --------
    vectorizer = get_tfidf_vectorizer()
    X_features = vectorizer.fit_transform(cleaned_texts)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_features, y, test_size=0.2, random_state=42
    )

    # Models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    best_model = None
    best_accuracy = 0

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        print(f"\n{name} Accuracy: {accuracy:.2f}")
        print(classification_report(y_test, predictions))

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model

    # -------- SAVE ARTIFACTS --------
    joblib.dump(best_model, "models/sentiment.pkl")
    joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

    print("\nBest model and vectorizer saved successfully.")


if __name__ == "__main__":
    train_and_evaluate()
