# input type: int
import sys

def main(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    output = main(input)
    print(output)