def list_files(current_filetree, current_path=""):
    answer_list = []
    for key, value in current_filetree.items():
        full_path = f"{current_path}/{key}"
        if value is None:
            answer_list.append(full_path)

        else:
            answer_list.extend(list_files(value, full_path))
    return answer_list
