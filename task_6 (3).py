def int_func(low_register_words):
    for word in low_register_words:
        print(word.title(), end=' ')


words = input('введите несколько слов, разделяя их пробелом: ').split(" ")
int_func(words)

