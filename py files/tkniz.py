import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re

def tknxz(problem_statement):
    # problem_statement = "This is a sample problem statement. It contains multiple sentences. Tokenization is necessary to break it down into tokens."
    word_tokens = word_tokenize(problem_statement)
    sentence_tokens = sent_tokenize(problem_statement)

    print("Word Tokens:")
    print(word_tokens)

    print("\nSentence Tokens:")
    print(sentence_tokens)

# Sample word tokens (after tokenization)
# word_tokens = ["This", "is", "a", "sample", "sentence", "with", "some", "punctuation", ".", "We", "are", "removing", "helping", "verbs", "like", "do", "and", "have", "."]

# Define a list of helping verbs
    helping_verbs = ["am", "is", "are", "was", "were", "be", "being", "been", "have", "has", "had", "do", "does", "did", "shall", "will", "should", "would", "may", "might", "must", "can", "could"]
    print("Chalja")
# Remove symbols using regular expressions
    word_tokens = [re.sub(r'[^\w\s]', '', token) for token in word_tokens]

# Remove helping verbs
    word_tokens = [token for token in word_tokens if token.lower() not in helping_verbs]
    print(word_tokens)
    return(word_tokens)