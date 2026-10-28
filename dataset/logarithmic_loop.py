# input type: int
import sys

def main(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    output = main(input)
    print(output)