def sum_nested_list(lst):
    list_cpy = lst.copy()
    sum = 0
    for item in list_cpy:
        if isinstance(item, list):
            sum += sum_nested_list(item)
        if isinstance(item, int):
            sum += item
    return sum
