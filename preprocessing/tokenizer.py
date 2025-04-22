from typing import List
import re

class Tokenizer:
    def __init__(self):
        self.separators = r'[\t \n]'
        self._stop_words_count = 50
        self._stop_words = None

    def tokenize(self, text: str) -> List[str]:
        tokens = [word for word in re.split(self.separators, text)]

        if self._stop_words != None:
            tokens = self.delete_stop_words(tokens)

        return tokens

    def detect_stop_words(self, tokens: List[str]):
        token_frequency = dict()
        for token in tokens:
            if token not in token_frequency:
                token_frequency[token] = 0
            token_frequency[token] += 1

        sorted_tokens = sorted(token_frequency.items(), key=lambda item: item[1], reverse=True)
        top_stop_words = dict(sorted_tokens[:self._stop_words_count])

        print("Stop words and their frequencies:")
        print(top_stop_words)
        print("Number of stop words detected:")
        print(len(top_stop_words))
        self._stop_words = top_stop_words.keys()

    def delete_stop_words(self, tokens: List[str]):
        filtered_tokens = []
        deleted_tokens = []
        for token in tokens:
            if token not in self._stop_words:
                filtered_tokens.append(token)
            else:
                deleted_tokens .append(token)
        return filtered_tokens

if __name__ == "__main__":
    text = "می روم، نمی خواهم به بیرون بروم."
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    print(tokens)