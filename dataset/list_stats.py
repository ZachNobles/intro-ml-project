# input type: list[int]
import sys
from collections import Counter

def main(numbers):
    if not numbers:
        return {"error": "List is empty"}

    differences = [
        numbers[i] - numbers[i - 1]
        for i in range(1, len(numbers))
    ]

    counts = Counter(numbers)

    return {
        "length": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
        "differences": differences,
        "ascending": all(a <= b for a, b in zip(numbers, numbers[1:])),
        "descending": all(a >= b for a, b in zip(numbers, numbers[1:])),
        "repeated": {n: c for n, c in counts.items() if c > 1}
    }

if __name__ == "__main__":
    input = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [2, 4, 6, 6, 10, 15]
    output = main(input)
    print(output)