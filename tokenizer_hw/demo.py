from tokenizer import TextTokenizer

def main():
    tokenizer = TextTokenizer()

    sample_text = "Hello, world! This is a test sentence. How are you today?" # пример текста для токенизации

    results = tokenizer.tokenize_all(sample_text) # применяем все методы токенизации
    
    for method, tokens in results.items(): # Выводим результаты
        print(f"\nРезультат {method}: \n{tokens}")

if __name__ == "__main__":
    main()