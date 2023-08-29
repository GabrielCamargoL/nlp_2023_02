import nltk
from nltk.stem import SnowballStemmer
import spacy
nlp = spacy.load("pt_core_news_sm")
stemmer = SnowballStemmer("portuguese")

examples = [
   "A empresa buscava novas estratégias",
  "A empresa buscou novas estratégias"
]

def stem_and_lemm(text):
    # Tokenização e stemming
    words = nltk.word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    
    # Lematização
    doc = nlp(text)
    lemmatized_words = [token.lemma_ for token in doc]
    
    return stemmed_words, lemmatized_words
  


print("--------------")
for text in examples:
    stemmed_result, lemmatized_result = stem_and_lemm(text)
    print("Texto original:", text)
    print("Stemming:", stemmed_result)
    print("Lemmatização:", lemmatized_result)
    print("="*50)