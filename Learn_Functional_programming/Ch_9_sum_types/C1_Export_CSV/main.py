from enum import Enum
from typing import List
from os import walk


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def convert_to_string_list(data: List[List[any]]) -> List[List[str]]:
    return [list(map(str, sublist)) for sublist in data]


def convert_to_csv(data: List[List[str]]) -> str:
    rows = [",".join(row) for row in data]
    csv_string = "\n".join(rows)
    return csv_string


def get_csv_status(status, data):
    match (status):
        case CSVExportStatus.PENDING:
            return ("Pending...", convert_to_string_list(data))
        case CSVExportStatus.PROCESSING:
            return ("Processing...", convert_to_csv(data))
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            return (
                "Unknown error, retrying...",
                convert_to_csv(convert_to_string_list(data)),
            )
        case _:
            raise Exception("Unknown export status")
