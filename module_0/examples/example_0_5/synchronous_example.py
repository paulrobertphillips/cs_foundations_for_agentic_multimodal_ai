import time

def fetch_data(name: str):
    print(f"Starting {name}")
    time.sleep(2)  # pretend this is a slow API call
    print(f"Finished {name}")

def main():
    fetch_data("task 1")
    fetch_data("task 2")
    fetch_data("task 3")

if __name__ == "__main__":
    main()