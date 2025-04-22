from index.term import Term
from typing import List
from tqdm import tqdm

class PosIndex:
    def __init__(self):
        self.word_term_map = dict()
        self.docs_length = dict()
        self.number_of_all_docs = 0

    def insert(self, doc: List[str], doc_id: int):
        self.number_of_all_docs += 1
        for pos, word in enumerate(doc):
            if word not in self.word_term_map.keys():
                self.word_term_map[word] = Term(id(word))
            self.word_term_map[word].insert(doc_id, pos)

    def calculate_idf(self):
        for key in tqdm(self.word_term_map.keys(), desc="Calculating IDF"):
            self.word_term_map[key].calculate_idf(self.number_of_all_docs)

    def calculate_champions_list(self, r=20):
        for key in tqdm(self.word_term_map.keys(), desc="Calculating Champions List"):
            self.word_term_map[key].calculate_champions_list(r)

    def post_process(self, r=20):
        self.calculate_idf()
        self.calculate_champions_list(r)

    def __str__(self):
        return f"{self.word_term_map}"
