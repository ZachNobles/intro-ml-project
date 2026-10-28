# input type: int
import sys
import secrets
import string

def main(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    output = main(input)
    print(output)