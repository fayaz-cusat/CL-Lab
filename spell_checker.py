import re
import nltk
from collections import defaultdict, Counter

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

class SpellChecker:
    def __init__(self, corpus):
        self.corpus = corpus.lower()
        self.vocab = set()
        self.bigram_freq = defaultdict(Counter)
        self._tokenize_and_create_vocab()
        self._create_bigram_freq()

    def _tokenize_and_create_vocab(self):
        """Tokenize the corpus and create a vocabulary."""
        tokens = nltk.word_tokenize(self.corpus)
        self.vocab = set(tokens)

    def _create_bigram_freq(self):
        """Create a bigram frequency table."""
        tokens = nltk.word_tokenize(self.corpus)
        for i in range(len(tokens) - 1):
            self.bigram_freq[tokens[i]][tokens[i + 1]] += 1

    def _edit_distance_candidates(self, word):
        """Generate candidates with one edit distance."""
        letters = 'abcdefghijklmnopqrstuvwxyz'
        candidates = set()

        # Deletions
        for i in range(len(word)):
            candidates.add(word[:i] + word[i + 1:])

        # Transpositions
        for i in range(len(word) - 1):
            candidates.add(word[:i] + word[i + 1] + word[i] + word[i + 2:])

        # Alterations
        for i in range(len(word)):
            for letter in letters:
                candidates.add(word[:i] + letter + word[i + 1:])

        # Insertions
        for i in range(len(word) + 1):
            for letter in letters:
                candidates.add(word[:i] + letter + word[i:])

        # Filter out candidates that are not in the vocabulary
        return candidates.intersection(self.vocab)

    def _bigram_probability(self, sentence):
        """Calculate the probability of a sentence using the bigram model."""
        tokens = nltk.word_tokenize(sentence)
        prob = 1.0
        for i in range(len(tokens) - 1):
            bigram_count = self.bigram_freq[tokens[i]].get(tokens[i + 1], 0)
            total_count = sum(self.bigram_freq[tokens[i]].values())
            prob *= (bigram_count / total_count) if total_count > 0 else 0
        return prob

    def correct(self, text):
        """Correct misspelled words in the input text."""
        tokens = nltk.word_tokenize(text)
        corrected_text = []

        for word in tokens:
            if word not in self.vocab:  # Check if the word is misspelled
                candidates = self._edit_distance_candidates(word)
                if candidates:
                    # Select the best candidate based on bigram probability
                    best_candidate = max(candidates, key=lambda candidate: self._bigram_probability(" ".join(corrected_text + [candidate])))
                    corrected_text.append(best_candidate)
                else:
                    corrected_text.append(word)  # No candidate found, keep the original
            else:
                corrected_text.append(word)  # Word is correctly spelled

        return " ".join(corrected_text)

# Example usage
corpus = """
This is a sample corpus for the spell checker. 
It contains several sentences. 
The quick brown fox jumps over the lazy dog.
Errors are bad.
"""

spell_checker = SpellChecker(corpus)
input_text = "Ths is a smple text with errrs."
corrected_text = spell_checker.correct(input_text)

print("Original Text:", input_text)
print("Corrected Text:", corrected_text)
