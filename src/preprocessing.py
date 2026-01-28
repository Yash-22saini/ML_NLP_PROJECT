import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLP resources (run once)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def clean_text(text: str) -> str:
    """
    Clean and preprocess input text.

    Steps:
    1. Convert to lowercase
    2. Remove punctuation and special characters
    3. Tokenize text
    4. Remove stopwords
    5. Lemmatize words
    """

    # 1. Lowercase
    text = text.lower()

    # 2. Remove punctuation & special characters
    text = re.sub(r'[^a-z\s]', '', text)

    # 3. Tokenization
    tokens = text.split()

    # 4. Stopword removal + 5. Lemmatization
    cleaned_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(cleaned_tokens)
