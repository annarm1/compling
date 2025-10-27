"""
Модуль для токенизации текста различными способами
"""

import re


class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        pass

    def simple_tokenize(self, text):
        """
        Простая токенизация по пробелам и знакам препинания

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов
        """
        tokens = re.findall(r"\b\w+\b", text) # ищет слова, разделенные пробелами и пунктуацией
        return tokens

    def nltk_tokenize(self, text):
        """
        Токенизация с использованием NLTK

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        from nltk.tokenize import word_tokenize
        import nltk
        nltk.download('punkt', quiet=True)
        tokens = word_tokenize(text) 
        return tokens

    def spacy_tokenize(self, text):
        """
        Токенизация с использованием spaCy

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        import spacy
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        return [token.text for token in doc]

    def tokenize_all(self, text):
        """
        Применяет все доступные методы токенизации

        Args:
            text (str): Входной текст

        Returns:
            dict: Словарь с результатами всех методов
        """
        return {"simple_tokenization": self.simple_tokenize(text),
            "nltk_tokenization": self.nltk_tokenize(text),
            "spacy_tokenization": self.spacy_tokenize(text)}


def demo():
    """Демонстрационная функция"""
    text = "Hello, world! This is a test sentence. How are you today?"

    tokenizer = TextTokenizer()
    results = tokenizer.tokenize_all(text)

    print("Результаты токенизации")
    for method, tokens in results.items():
        print(f"\nРезультат {method}:")
        print(tokens)


if __name__ == "__main__":
    demo()