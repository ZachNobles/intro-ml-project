# input type: list[str]
import sys

def main(items):
    return items[::-1]

if __name__ == "__main__":
    input = sys.argv[1:] if len(sys.argv) > 1 else ["red", "green", "blue"]
    output = main(input)
    print(output)