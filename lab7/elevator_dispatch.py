
def parse_request(text):
    if not isinstance(text, str):
        return None

    try:
        start, end = text.split("->")
        return int(start), int(end)
    except ValueError:
        return None


def total_travel(floors_csv):
    if not isinstance(floors_csv, str) or not floors_csv.strip():
        return None

    try:
        floors = [int(f) for f in floors_csv.split(",")]
    except ValueError:
        return None

    return sum(
        abs(floors[i + 1] - floors[i])
        for i in range(len(floors) - 1)
    )


def load_percent(text):
    if not isinstance(text, str):
        return None

    try:
        load, capacity = text.split(" of ")
        load = int(load)
        capacity = int(capacity)
    except ValueError:
        return None

    if capacity <= 0 or load < 0:
        return None

    return load * 100 // capacity


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    print("Load Percent:", result)


if __name__ == "__main__":
    main()
