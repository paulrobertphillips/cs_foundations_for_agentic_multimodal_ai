def filter_rows(rows):
    return [r for r in rows if float(r["value"]) > 10]