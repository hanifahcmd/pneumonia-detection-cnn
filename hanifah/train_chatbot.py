import json
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

with open('intents.json') as f:
    intents = json.load(f)

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)

    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1
    return bag

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

# stemming
all_words = sorted(set([stem(w) for w in all_words]))

print("Training completed.")
print("Total tags:", tags)
print("Vocabulary size:", len(all_words))

# Save metadata
metadata = {
    "words": all_words,
    "tags": tags
}

with open("metadata.json", "w") as f:
    json.dump(metadata, f)

print("Metadata saved to metadata.json")