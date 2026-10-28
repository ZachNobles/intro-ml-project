# input type: int
import sys
import random
import time

def main(n):
    a = [[random.random() for _ in range(n)] for _ in range(n)]
    b = [[random.random() for _ in range(n)] for _ in range(n)]
    c = [[0.0] * n for _ in range(n)]

    start = time.perf_counter()

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    elapsed = time.perf_counter() - start

    return {
        "size": n,
        "sample": c[0][:5] if n else [],
        "elapsed_seconds": elapsed
    }

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    if not 0 <= input <= 300:
        raise SystemExit("Matrix size must be between 0 and 300")
    output = main(input)
    print(output)