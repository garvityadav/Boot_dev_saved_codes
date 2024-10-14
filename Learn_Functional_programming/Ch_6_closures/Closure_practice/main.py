def new_collection(initial_docs):
    copy = initial_docs.copy()

    def new_list(string):
        copy.append(string)
        return copy

    return new_list
