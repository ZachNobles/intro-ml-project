# input type: list[int]
import sys

def main(data):
    return sorted(data)

if __name__ == "__main__":
    input = sys.argv[1:] if len(sys.argv) > 1 else [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    input = [int(x) for x in input]
    output = main(input)
    print(output)