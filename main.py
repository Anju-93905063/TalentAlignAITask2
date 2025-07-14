import fitz
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

abbreviation_map = {
    "js": "javascript",
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "sql": "structured query language",
    "db": "database"
}

def extract_text(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = text.split()
    words = [abbreviation_map.get(word, word) for word in words if word not in stop_words]
    return ' '.join(words)

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return similarity[0][0]

if __name__ == "__main__":
    resume_text = extract_text("sample_resume.pdf")
    jd_text = extract_text("sample_jd.pdf")

    resume_clean = preprocess(resume_text)
    jd_clean = preprocess(jd_text)

    score = calculate_similarity(resume_clean, jd_clean)
    print(f"\n🔍 Resume-JD Similarity Score: {score:.2f} (out of 1.0)\n")
