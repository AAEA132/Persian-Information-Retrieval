from preprocessing.preprocess import preprocess
from index.posIndex import PosIndex
from index.documentList import DocumentList
import math

def calculate_query_weights(preprocessed_query, main_posIndex, main_documents):
    query_tfs = dict()
    query_weights = dict()
    for word in preprocessed_query:
        if word not in main_posIndex.word_term_map:
            continue
        if word not in query_tfs.keys():
            query_tfs[word] = 0
        query_tfs[word] += 1

    for word in query_tfs.keys():
        query_weights[word] = ((1 + math.log(query_tfs[word])) *
                               main_posIndex.word_term_map[word].idf)
    return query_weights

def query_process(query: str, main_posIndex: PosIndex, main_documents: DocumentList, k=100):
    docs_scores = dict()
    preprocessed_query = preprocess(query)
    query_weights = calculate_query_weights(preprocessed_query, main_posIndex, main_documents)
    for word in preprocessed_query:
        if word not in main_posIndex.word_term_map:
            continue
        term = main_posIndex.word_term_map[word]
        for doc_id in term.champions_list:
            if doc_id not in docs_scores:
                docs_scores[doc_id] = 0
            docs_scores[doc_id] += query_weights[word] * (
                    term.idf * (1 + math.log(term.docIdToPositionsMap[doc_id].tf_of_t_and_d)))
    for doc_id in docs_scores:
        docs_scores[doc_id] /= main_posIndex.docs_length[doc_id]
    document_list = []
    scores = []
    for i in range(k):
        if docs_scores.__len__() == 0:
            break
        max_n = 0
        max_k = None
        for doc_id in docs_scores:
            if docs_scores[doc_id] > max_n:
                max_n = docs_scores[doc_id]
                max_k = doc_id

        scores.append(docs_scores[max_k])
        docs_scores.pop(max_k)
        document_list.append(main_documents.doc_dict[max_k])
    return document_list, scores

def query_process2(query: str, main_posIndex: PosIndex, main_documents: DocumentList, k=20):
    docs_scores = dict()
    preprocessed_query = preprocess(query)
    query_weights = calculate_query_weights(preprocessed_query, main_posIndex, main_documents)
    for word in preprocessed_query:
        if word not in main_posIndex.word_term_map:
            continue
        term = main_posIndex.word_term_map[word]
        for doc_id in term.docIdToPositionsMap:
            if doc_id not in docs_scores:
                docs_scores[doc_id] = 0
            docs_scores[doc_id] += query_weights[word] * (
                    term.idf * (1 + math.log(term.docIdToPositionsMap[doc_id].tf_of_t_and_d)))

    i = 0
    for doc_id in docs_scores:
        docs_scores[doc_id] /= main_posIndex.docs_length[doc_id]
        if (i < 10):
            print(main_posIndex.word_term_map[word].docIdToPositionsMap[doc_id])
            i += 1

    document_list = []

    return document_list
