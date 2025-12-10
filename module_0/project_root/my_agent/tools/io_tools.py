import csv

def load_csv(path: str):
    with open(path, "r") as f:
        return list(csv.DictReader(f))
