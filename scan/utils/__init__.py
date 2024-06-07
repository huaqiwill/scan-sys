import datetime
import json
from django.db import models


def get_filters(params: str, fields: list[str]):
    filters = {}
    if params not in [None, ""]:
        req = json.loads(params)
        for field in fields:
            if req.get(field) not in [None, ""]:
                filters[field] = req[field]
    return filters


def get_datetime(model: datetime.datetime):
    if model is None:
        return ""
    return model.strftime('%Y-%m-%d %H:%M:%S')
