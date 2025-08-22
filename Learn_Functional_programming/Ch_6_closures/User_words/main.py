def user_words(initial_words):

    def add_word(word):
        nonlocal initial_words
        initial_words = initial_words + (word,)
        return initial_words

    return add_word
