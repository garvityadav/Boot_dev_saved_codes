def word_count_aggregator():
    count = 0

    def word_count(doc):
        nonlocal count
        copy_doc = doc
        count += len(copy_doc.split(" "))
        return count

    return word_count
