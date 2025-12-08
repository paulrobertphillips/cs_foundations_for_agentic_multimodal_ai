# Module 0.1 — Python Packaging Basics

### 🧪 Mini-Exercise

Organize this single-file script into a package with a tools/ and processing/ folder:
```
import csv

def read_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def filter_rows(rows):
    return [r for r in rows if float(r["value"]) > 10]

def main():
    rows = read_csv("data.csv")
    print(filter_rows(rows))

main()

```
If you want, I can walk you through the solution step-by-step.