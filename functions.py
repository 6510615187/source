def my_max(data: list) -> None:
    current_max = data[0]
    for item in data:
        if item > current_max:
            current_max = item
    print(f"Data: {data}")
    print(f"Maximum: {current_max}")


def my_min(data: list) -> None:
    current_min = data[0]
    for item in data:
        if item < current_min:
            current_min = item
    print(f"Data: {data}")
    print(f"Minimum: {current_min}")

def my_sum(data: list) -> None:
    total = 0
    for item in data:
        total += item
    print(f"Data: {data}")
    print(f"Sum: {total}")
