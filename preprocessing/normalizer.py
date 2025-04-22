import re

class Normalizer:
    def __init__(self):
        self.punctuations = {char: ' ' for char in '٫٬؛!"#$%&\'()*+,-./:;<=>?[\\]^_`{|}~،><«»؟《》“'}

        self.erabs = {
            '\u064B': '',  # Fathatan
            '\u064C': '',  # zammatan
            '\u064D': '',  # Kasratan
            '\u064E': '',  # Fathe
            '\u064F': '',  # Zamme
            '\u0650': '',  # Kasre
            '\u0651': '',  # Tashdid
            '\u0652': '',  # Sukuns
            '\u0653': '',  # Maddah above
            '\u0654': '',  # Hamza above
            '\u0655': '',  # Hamza below
        }
        self.numbers = {
            '0': '۰',
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹',
            '%': '٪',
        }
        self.useless_unicodes = {
            '\u061F' : '', # arabic question mark
            '\u200F' : '', # left to right
            '\u200E' : '', # right to left
            '\u202B' : '', # right to left embedding
            '\u2069' : '', # Pop directoral isolate character
            '\u202C' : '', # Pop directoral formatting character
            '\u2067' : '', # right to left isolate
            '\u202A' : '', # left to right embedding
        }
        self.alphabets = {
            "آ": "آ",
            "ﺁ": "آ",
            "ك": "ک",
            "ڪ": "ک",
            "ﮐ": "ک",
            "ﮑ": "ک",
            "ﻛ": "ک",
            "ګ": "ک",
            "ﮏ": "ک",
            "ﻜ": "ک",
            "ﮎ": "ک",
            "ﻚ": "ک",
            "ڭ": "ک",
            "ي": "ی",
            "ى": "ی",
            "ے": "ی",
            "ێ": "ی",
            "ﯿ": "ی",
            "ﯾ": "ی",
            "ﯽ": "ی",
            "ې": "ی",
            "ﯼ": "ی",
            "ﻴ": "ی",
            "ﻳ": "ی",
            "ں": "ی",
            "ﻲ": "ی",
            "ﻱ": "ی",
            "ﻰ": "ی",
            "ۍ": "ی",
            "ﻯ": "ی",
            "ﭛ": "ی",
        }
        self.polymorphism_words = {
            "﷼": "ریال",
            "أ" : "ا",
            "ة": "ه",
            "طهران": "تهران",
            "باطری": "باتری",
            "کتاب خانه": "کتابخانه",
            "گفت و گو": "گفتگو",
            "جست و جو": "جستجو",
            "شست و شو": "شستشو",
            "اطاق": "اتاق",
            "امپراطور": "امپراتور",
            "علیرغم": "علی‌رغم",
            "پیشبینی": "پیش‌بینی",
            "بیصدا": "بی‌صدا",
        }
        self.suffixes = [
            "ای",
            "ها",
            "های",
            "هایی",
            "تر",
            "تری",
            "ترین",
            "گر",
            "گری",
            "ام",
            "ات",
            "اش",
        ]
        self.prefixes = [
            "می",
            "نمی"
        ]

    def normalize(self, text:str):
        for punc in self.punctuations:
            text = text.replace(punc, self.punctuations.get(punc))

        for erab in self.erabs:
            text = text.replace(erab, self.erabs.get(erab))

        for number in self.numbers:
            text = text.replace(number, self.numbers.get(number))

        # Add space before and after numbers
        text = re.sub(r'(\d+)', r' \1 ', text)

        for useless_unicode in self.useless_unicodes:
            text = text.replace(useless_unicode, self.useless_unicodes.get(useless_unicode))

        for polymorphism_word in self.polymorphism_words:
            text = text.replace(polymorphism_word, self.polymorphism_words.get(polymorphism_word))

        for alphabet in self.alphabets:
            text = text.replace(alphabet, self.alphabets.get(alphabet))

        for suffixe in self.suffixes:
            text = text.replace(" " + suffixe, "\u200c" + suffixe)

        for prefix in self.prefixes:
            text = text.replace(prefix + " ", prefix + "\u200c")

        return text
    

