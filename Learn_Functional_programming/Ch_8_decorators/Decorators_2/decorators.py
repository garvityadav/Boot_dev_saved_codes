def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        new_list = list(map(lambda x: convert_md_to_txt(x), args))
        new_dict = {k: convert_md_to_txt(v) for k, v in kwargs.items()}
        return func(*new_list, **new_dict)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
