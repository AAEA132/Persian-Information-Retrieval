import math


class TermPositionsInDoc:
    def __init__(self, doc_id: int, term_id: int):
        self.doc_id = doc_id
        self.term_id = term_id
        self.tf_of_t_and_d = 0
        self.positions = []

    def insert(self, position: int):
        self.tf_of_t_and_d += 1
        self.positions.append(position)

    def __str__(self):
        return f"{self.doc_id}: {self.positions}\n"


class Term:
    def __init__(self, term_id: int):
        self.term_id = term_id
        self.term_df = 0
        self.docIdToPositionsMap = dict()
        self.champions_list = dict()
        self.idf = 0

    def insert(self, doc_id: int, position: int):
        if doc_id not in self.docIdToPositionsMap.keys():
            self.term_df += 1
            self.docIdToPositionsMap[doc_id] = TermPositionsInDoc(doc_id, self.term_id)
        self.docIdToPositionsMap[doc_id].insert(position)

    def calculate_idf(self, number_of_all_docs: int):
        self.idf = math.log(number_of_all_docs / self.term_df)

    def calculate_champions_list(self, r=20):
        sorted_doc_terms = sorted(self.docIdToPositionsMap.items(), key=lambda x: x[1].tf_of_t_and_d, reverse=True)
        top_20_doc_terms = sorted_doc_terms[:r]
        self.champions_list = dict(top_20_doc_terms)

    def __str__(self):
        term_string = f"{self.term_id}:\n"
        for key in self.docIdToPositionsMap.keys():
            term_string += self.docIdToPositionsMap[key].__str__()
        return term_string
