# input type: list[str]
import sys

def main(items):
    return list(dict.fromkeys(items))

if __name__ == "__main__":
    input = sys.argv[1:] if len(sys.argv) > 1 else ["apple", "banana", "apple", "orange"]
    output = main(input)
    print(output)