# input type: int
import sys
import math

def main(limit):
    primes = []

    for n in range(2, limit + 1):
        is_prime = True

        for divisor in range(2, math.isqrt(n) + 1):
            if n % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(n)

    return primes

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    output = main(input)
    print(output)