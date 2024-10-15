from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    document_copy = document.split('\n')
    start = 0
    end = 0
    line_number = 0
    if 'start' in edit.keys():
        start = edit['start']
    if 'end' in edit.keys():
        end = edit['end']
    if 'line_number' in edit.keys():
        line_number = edit['line_number']

    def check_start_end(start, end, target_len):
        if target_len < start:
            raise Exception('Invalid start index')
        if target_len < end or end < start:
            raise Exception('Invalid end index')

    if line_number >= len(document_copy):
        raise Exception('Invalid line number')

    if edit_type == EditType.NEWLINE:
        document_copy.insert(line_number+1, "")
        document_copy = "\n".join(document_copy)
        return document_copy

    if edit_type == EditType.SUBSTITUTE:
        temp_string = document_copy[line_number]
        check_start_end(start, end, len(temp_string))

        document_copy[line_number] = temp_string[:start
                                                 ]+edit['insert_text']+temp_string[end:]
        document_copy = "\n".join(document_copy)

        return document_copy

    if edit_type == EditType.INSERT:
        temp_string = document_copy[line_number]
        check_start_end(start, end, len(temp_string))

        document_copy[line_number] = temp_string[:start
                                                 ]+edit['insert_text']+temp_string[start:]
        document_copy = '\n'.join(document_copy)
        return document_copy

    if edit_type == EditType.DELETE:
        temp_string = document_copy[line_number]
        check_start_end(start, end, len(temp_string))
        document_copy[line_number
                      ] = temp_string[:start]+temp_string[end:]
        document_copy = '\n'.join(document_copy)
        return document_copy

    # exceptions
    else:
        raise Exception('Unknown edit type')
