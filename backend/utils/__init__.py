import datetime

def to_datetime(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f")

def to_jsondate(d: datetime.datetime) -> str:
    return d.strftime('%Y-%m-%dT%H:%M:%S.%f')