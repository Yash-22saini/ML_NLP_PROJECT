#from sklearn.feature_extraction.text import TfidfVectorizer
#from src.preprocessing import clean_text


#def get_tfidf_vectorizer():
#    """
#   Creates and returns a TF-IDF vectorizer.
#   """
#   vectorizer = TfidfVectorizer(
#       ngram_range=(1, 2),   # unigrams + bigrams
#       max_features=5000
#   )
#   return vectorizer


#def preprocess_and_vectorize(texts, vectorizer):
#    """
#   Cleans text and applies TF-IDF.
#   """
#   cleaned_texts = [clean_text(text) for text in texts]
#   features = vectorizer.fit_transform(cleaned_texts)
#   return features##

#def preprocess_text(text: str) -> str:
#   import re
#   text = text.lower()
#   text = re.sub(r"[^a-zA-Z\s]", "", text)
#   return text



from sklearn.feature_extraction.text import TfidfVectorizer
import re


def get_tfidf_vectorizer():
    """
    Creates and returns a TF-IDF vectorizer (used during training only).
    """
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000
    )
    return vectorizer


def preprocess_text(text: str) -> str:
    """
    Cleans text for inference (NO fitting here).
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text
