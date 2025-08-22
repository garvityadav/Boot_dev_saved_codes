from functools import reduce


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")

    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


# don't touch above this line


def create_html_table(data_rows):
    data_cell = map(lambda x: accumulate_data_cells(x), data_rows)
    table_rows = accumulate_rows(data_cell)

    def create_table_headers(headers):
        nonlocal table_rows
        header_data = accumulate_headers(headers)
        data_rows = tag_row(header_data)
        return tag_table(f"{data_rows}{table_rows}")

    return create_table_headers
