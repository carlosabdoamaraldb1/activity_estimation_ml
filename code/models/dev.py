from fuzzywuzzy import fuzz
import json
from data.dev import developer_dict


class Developer:
    def __init__(
        self,
        name: str,
        seniority: str,
        stack: str,
        capacity: int,
    ) -> None:
        self.name = name
        self.seniority = seniority
        self.stack = stack
        self.capacity = capacity


def get_dev_by_name(name: str) -> Developer:
    ks: list[str] = developer_dict.keys()

    greatest_similarity: int = 0
    most_similar_name: str = ''
    for key in ks:
        similarity = fuzz.partial_token_sort_ratio(key, name)

        if similarity > greatest_similarity:
            greatest_similarity = similarity
            most_similar_name = key

    try:
        dev = developer_dict[f"{most_similar_name.lower()}"]
        return Developer(
            dev["name"],
            dev["seniority"],
            dev["stack"],
            dev["capacity"]
        )
    except:
        print("Developer name looks not right")
        return None
