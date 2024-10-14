from functools import reduce


def paginator(page_length):
    def paginate(document):
        words = document.split()

        def add_word_to_pages(pages, word):
            if not pages or len(pages[-1]) + len(word) + 1 > page_length:
                pages.append(word)
            else:
                pages[-1] += f" {word}"
            return pages

        return reduce(add_word_to_pages, words, [])

    return paginate
