import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from speak import speak
import warnings as wrn
wrn.filterwarnings('ignore')

def load_dataset(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = []
        for line in lines:
            line = line.strip()
            if ':' in line:
                # Split only on the first occurrence of ':'
                q, a = line.split(':', 1)
                qna_pairs.append({'question': q.strip(), 'answer': a.strip()})
    return qna_pairs


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text)
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)  # Join with a space to form a proper sentence

def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]  # Fixed key error
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']

def mind(text):
    dataset_path = r'C:\Users\user\OneDrive\Desktop\J.A.R.V.I.S\Computation\qna_data.txt'
    dataset = load_dataset(dataset_path)

    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, X, dataset)
    print(answer)
    return answer
