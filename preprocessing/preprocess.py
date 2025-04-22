from preprocessing.tokenizer import Tokenizer
from preprocessing.normalizer import Normalizer
from hazm import lemmatizer

tokenizer = Tokenizer()
normalizer = Normalizer()
stemmer = lemmatizer.Lemmatizer()


def detect_stop_words(content):
    tokenizer.detect_stop_words(content)

def preprocess(content):
    normalized_content = normalizer.normalize(content)
    tokenized_content = tokenizer.tokenize(normalized_content)
    lemmatized_content = [stemmer.lemmatize(token) for token in tokenized_content]
    return lemmatized_content