# input type: str
import sys

def main(n):
    print("*" * (len(str(n)) + 6))
    print("** " + str(n) + " **")
    print("*" * (len(str(n)) + 6))

if __name__ == "__main__":
    input = sys.argv[1] if len(sys.argv) > 1 else "Hello World"
    main(input)