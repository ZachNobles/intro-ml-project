# input type: int
import sys
import random

def main(n):
    n = max(10, n)
    rng = random.Random(42)
    k = 8
    points = [
        (rng.random() * 100, rng.random() * 100)
        for _ in range(n)
    ]
    centers = points[:k]

    for _ in range(30):
        sums = [[0.0, 0.0, 0] for _ in range(k)]

        for x, y in points:
            best = min(
                range(k),
                key=lambda c: (
                    (x - centers[c][0]) ** 2
                    + (y - centers[c][1]) ** 2
                )
            )
            sums[best][0] += x
            sums[best][1] += y
            sums[best][2] += 1

        centers = [
            (s[0] / s[2], s[1] / s[2])
            if s[2] else centers[i]
            for i, s in enumerate(sums)
        ]

    inertia = 0.0
    for x, y in points:
        inertia += min(
            (x - cx) ** 2 + (y - cy) ** 2
            for cx, cy in centers
        )

    return round(inertia, 6)

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    output = main(input)
    print(output)