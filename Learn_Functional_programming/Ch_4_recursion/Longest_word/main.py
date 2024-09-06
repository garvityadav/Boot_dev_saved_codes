def find_longest_word(document, longest_word=""):
    word_list = document
    word_list = word_list.split(" ")
    if len(document) <= 0:
        return longest_word
    if len(longest_word) < len(word_list[0]):
        longest_word = word_list[0]
    return find_longest_word(" ".join(word_list[1:]), longest_word)
