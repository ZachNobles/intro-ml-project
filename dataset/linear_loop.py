# input type: int
import sys

def main(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    output = main(input)
    print(output)