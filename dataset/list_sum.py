# input type: list[int]
import sys

def main(numbers):
    return sum(numbers)

if __name__ == "__main__":
    input = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [1, 2, 3, 4, 5]
    output = main(input)
    print(output)