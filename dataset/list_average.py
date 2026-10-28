# input type: list[float]
import sys

def main(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == "__main__":
    input = [float(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [10, 20, 30]
    output = main(input)
    print(output)