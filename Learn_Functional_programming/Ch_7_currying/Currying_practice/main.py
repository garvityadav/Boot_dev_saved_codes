from functools import reduce


def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.splitlines()
            return reduce(lambda count, line: count + (sequence in line), lines, 0)

        return with_length

    return with_char
