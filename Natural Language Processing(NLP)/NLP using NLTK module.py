"""
A comprehensive script illustrating basic NLP preprocessing steps:
1. Segmentation (sentences & paragraphs)
2. Tokenization (word tokens)
3. Stop-word removal
4. Stemming
5. Lemmatization
6. POS tagging
7. Named Entity Recognition (NER)
8. Text normalization (lowercasing, Unicode)
9. Contraction expansion
10. Regular Expression extraction
11. Chunking & Chinking
12. WordNet synsets & relations

Dependencies:
    pip install nltk contractions
"""

#!/usr/bin/env python3

import re
import unicodedata
import contractions
import nltk

# ── Ensure required NLTK data is available ──
nltk.download('punkt',       quiet=True)   # tokenizers
nltk.download('stopwords',   quiet=True)   # stop‐word lists
nltk.download('averaged_perceptron_tagger_eng', quiet=True)  # POS tagger
nltk.download('maxent_ne_chunker_tab', quiet=True)           # NER chunker model
nltk.download('words',                  quiet=True)   # for NER
nltk.download('wordnet',                quiet=True)   # lemmatizer
nltk.download('omw-1.4',                quiet=True)   # WordNet data
# ── End downloads ──

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet as wn
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.chunk import ne_chunk, RegexpParser

# … rest of your functions and __main__ block …

def segmentation_examples(text):
    """1. Sentence & Paragraph Segmentation"""
    sentences = sent_tokenize(text)
    paragraphs = text.split('\n\n')
    return sentences, paragraphs

def tokenization_example(sentence):
    """2. Word-based Tokenization"""
    return word_tokenize(sentence)

def remove_stopwords(tokens):
    """3. Stop-word Removal"""
    stop_words = set(stopwords.words('english'))
    return [t for t in tokens if t.lower() not in stop_words]

def stemming_example(words):
    """4. Porter Stemming"""
    ps = PorterStemmer()
    return [ps.stem(w) for w in words]

def lemmatization_example(tokens):
    """5. Lemmatization (with basic POS handling)"""
    wnl = WordNetLemmatizer()
    lemmas = []
    for t in tokens:
        pos = 'a' if t.lower() == 'better' else 'n'
        lemmas.append(wnl.lemmatize(t, pos=pos))
    return lemmas

def pos_tagging_example(text):
    """6. POS Tagging"""
    tokens = word_tokenize(text)
    return nltk.pos_tag(tokens)

def ner_example(text):
    """7. Named Entity Recognition"""
    tags = pos_tagging_example(text)
    return ne_chunk(tags)

def normalize_text(raw):
    """8. Lowercase, Unicode Normalize"""
    lower = raw.lower()
    norm = unicodedata.normalize('NFC', lower)
    return norm

def expand_contractions(text):
    """9. Contraction Expansion"""
    return contractions.fix(text)

def regex_extraction(text):
    """10. Regex: emails & dates"""
    emails = re.findall(r'\S+@\S+\.\S+', text)
    dates  = re.findall(r'\d{4}-\d{2}-\d{2}', text)
    return emails, dates

def chunking_chinking_example(text):
    """11. Chunking & Chinking for Noun Phrases"""
    tokens = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    grammar = r"NP: {<DT>?<JJ>*<NN>+}"
    parser = RegexpParser(grammar)
    return parser.parse(pos_tags)

def wordnet_example(word):
    """12. WordNet: synsets, lemmas, hypernyms, antonyms"""
    syns = wn.synsets(word)
    if not syns:
        return {}
    s0 = syns[0]
    return {
        'definition': s0.definition(),
        'lemmas': [l.name() for l in s0.lemmas()],
        'hypernyms': [h.name() for h in s0.hypernyms()],
        'antonyms': [a.name() for l in s0.lemmas() for a in l.antonyms()]
    }

if __name__ == "__main__":
    # Sample inputs
    sample_paragraph = (
        "Hello there! How are you doing today? I hope you’re well.\n\n"
        "This is the second paragraph. It has two sentences."
    )
    sample_sentence = "GPT-3, released in 2020, revolutionized NLP!"
    sample_text = "It is a sunny day, and I don't want to waste it."
    sample_ner = "Apple Inc. was founded by Steve Jobs in Cupertino in 1976."
    sample_chunk = "The seasoned software engineer fixed the bug quickly."
    sample_word = "dog"

    # Run examples
    sents, paras = segmentation_examples(sample_paragraph)
    tokens = tokenization_example(sample_sentence)
    filtered = remove_stopwords(tokens)
    stems = stemming_example(["connect", "connected", "connecting", "connection"])
    lemmas = lemmatization_example(["better", "running", "geese"])
    pos = pos_tagging_example(sample_sentence)
    ner_tree = ner_example(sample_ner)
    normalized = normalize_text("I Can't wait to analyse this café’s menu!")
    expanded = expand_contractions(sample_text)
    emails, dates = regex_extraction("Contact: support@example.com on 2025-05-03.")
    chunked = chunking_chinking_example(sample_chunk)
    wn_info = wordnet_example(sample_word)

    # Print outputs
    print("Sentences:", sents)
    print("Paragraphs:", paras)
    print("Tokens:", tokens)
    print("Filtered Tokens:", filtered)
    print("Stemmed:", stems)
    print("Lemmatized:", lemmas)
    print("POS Tags:", pos)
    print("NER Tree:", ner_tree)
    print("Normalized Text:", normalized)
    print("Expanded Contractions:", expanded)
    print("Emails & Dates:", emails, dates)
    print("Chunked NP:", chunked)
    print("WordNet Info:", wn_info)
