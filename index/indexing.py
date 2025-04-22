import json
import pickle
from preprocessing.preprocess import tokenizer
from preprocessing.preprocess import normalizer
from preprocessing.preprocess import preprocess, detect_stop_words
from index.posIndex import PosIndex
from index.documentList import DocumentList
from tqdm import tqdm

def read_json(path):
    file = open(path)
    data = json.load(file)
    return data


def index(path='data/document_collection.json'):
    posIndex = PosIndex()
    documents = DocumentList()

    data = read_json(path)

    all_content = ''
    for i in tqdm(data, desc="Processing all content for stop words"):
        all_content += data[i]['content']
    normalized_content = normalizer.normalize(all_content)
    tokenized_content = tokenizer.tokenize(normalized_content)
    detect_stop_words(tokenized_content)

    for doc_id in tqdm(data, desc="Indexing documents"):
        content = data[doc_id]['content']
        documents.insert(doc_id, data[doc_id]['title'], data[doc_id]['content'], data[doc_id]['category'],
                         data[doc_id]['url'])
        preprocessed_content = preprocess(content)
        posIndex.docs_length[doc_id] = preprocessed_content.__len__()
        posIndex.insert(preprocessed_content, doc_id)

    posIndex.post_process()

    with open('data/posIndex.pkl', 'wb') as file:
        pickle.dump(posIndex, file)

    with open('data/documents.pkl', 'wb') as file:
        pickle.dump(documents, file)

    return posIndex, documents


def detect_s_words(path='data/document_collection.json'):

    data = read_json(path)

    all_content = ''
    for i in tqdm(data, desc="Processing all content for stop word detection"):
        all_content += data[i]['content']

    detect_stop_words(all_content)