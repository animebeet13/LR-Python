# TODO решите задачу
import json


def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    summa = sum([i["score"] * i["weight"] for i in json_data])
    return round(summa, 3)


print(task())
