# input type: int
import sys
import random
import time

def main(n):
    data = [random.randint(0, 100000) for _ in range(n)]

    start = time.perf_counter()
    sorted(data)
    builtin_time = time.perf_counter() - start

    items = data.copy()
    start = time.perf_counter()

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

        if not swapped:
            break

    bubble_time = time.perf_counter() - start

    return {
        "built_in_seconds": builtin_time,
        "bubble_sort_seconds": bubble_time
    }

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    output = main(input)
    print(output)