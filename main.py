from index import indexing
from query_processing.queryProcess import query_process
import pickle

def load_indexing():
    try:
        with open('data/posIndex.pkl', 'rb') as file:
            loaded_posIndex = pickle.load(file)

        with open('data/documents.pkl', 'rb') as file:
            loaded_documents = pickle.load(file)

        return loaded_posIndex, loaded_documents
    except FileNotFoundError:
        return None, None

def main_loop():
    main_posIndex, main_documents = load_indexing()

    if main_posIndex is None or main_documents is None:
        main_posIndex, main_documents = indexing.index()
    else:
        indexing.detect_s_words()

    while True:
        print('Query : ')
        query = str(input())
        documents_list, score_list = query_process(query, main_posIndex, main_documents)
        with open(f'data/{query}.txt', 'w', encoding='utf-8') as file:
            for document, score in zip(documents_list, score_list):
                print(f"Sim score: {score}")
                print(document, file=file)

if __name__ == "__main__":
    main_loop()