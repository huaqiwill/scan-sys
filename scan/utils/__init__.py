import json


def get_filters(params: str, fields: list[str]):
    filters = {}
    if params not in [None, ""]:
        req = json.loads(params)
        for field in fields:
            if req.get(field) not in [None, ""]:
                filters[field] = req[field]
    return filters
