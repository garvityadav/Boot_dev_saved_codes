def create_markdown_image(alt_text):
    text = f"![{alt_text}]"

    def inner_fun(url):
        nonlocal text
        url_text = url.replace("(", "%28").replace(")", "%29")
        url_text = f"{text}({url_text})"

        def innermost_fun(title=""):
            nonlocal url_text
            if title:
                url_text = url_text.replace(")", f' "{title}")')

            return url_text

        return innermost_fun

    return inner_fun
