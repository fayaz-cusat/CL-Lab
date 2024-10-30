import nltk
from nltk.corpus import movie_reviews
import random

# Download the movie reviews dataset
nltk.download('movie_reviews')

# Load the dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents
random.shuffle(documents)

# Split into train and test sets
train_set = documents[:1500]
test_set = documents[1500:]


from collections import defaultdict

def get_words_in_documents(documents):
    all_words = []
    for words, _ in documents:
        all_words.extend(words)
    return all_words

def get_word_features(word_list):
    wordlist = nltk.FreqDist(word_list)
    return list(wordlist.keys())

all_words = get_words_in_documents(train_set)
word_features = get_word_features(all_words)

class NaiveBayesClassifier:
    def __init__(self, k=1):
        self.k = k
        self.word_counts = defaultdict(lambda: defaultdict(int))
        self.category_counts = defaultdict(int)
        self.total_documents = 0
        self.vocab_size = 0

    def train(self, documents):
        for words, category in documents:
            self.category_counts[category] += 1
            self.total_documents += 1
            for word in words:
                self.word_counts[category][word] += 1

        # Vocabulary size
        self.vocab_size = len(word_features)

    def predict(self, document):
        category_probs = {}
        for category in self.category_counts:
            # Calculate log probabilities
            log_prob = 0
            for word in document:
                word_count = self.word_counts[category].get(word, 0)
                log_prob += (word_count + self.k) / (self.category_counts[category] + self.k * self.vocab_size)
            category_probs[category] = log_prob + self.category_counts[category] / self.total_documents

        return max(category_probs, key=category_probs.get)


def evaluate_classifier(k):
    classifier = NaiveBayesClassifier(k)
    classifier.train(train_set)
    
    correct_predictions = 0
    total_predictions = len(test_set)

    for words, actual_category in test_set:
        predicted_category = classifier.predict(words)
        if predicted_category == actual_category:
            correct_predictions += 1

    accuracy = correct_predictions / total_predictions
    return accuracy

k_values = [0.25, 0.75, 1.0]
results = {}

for k in k_values:
    accuracy = evaluate_classifier(k)
    results[k] = accuracy
    print(f'Accuracy for k={k}: {accuracy:.2f}')
