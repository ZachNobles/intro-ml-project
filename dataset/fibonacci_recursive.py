# input type: int
import sys

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = fibonacci(n - 1)
    next_number = sequence[-1] + (sequence[-2] if len(sequence) > 1 else 1)
    sequence.append(next_number)

    return sequence

def main(n):
    return fibonacci(n)

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    output = main(input)
    print(output)