# input type: int
import sys
import random
import math

def main(n):
    n = max(2, n)
    rng = random.Random(42)

    count = min(n, 1000)
    steps = n
    positions = [
        [rng.random() * 100, rng.random() * 100]
        for _ in range(count)
    ]
    velocities = [
        [0.0, 0.0] for _ in range(count)
    ]
    masses = [rng.random() + 0.5 for _ in range(count)]

    dt = 0.001
    softening = 0.01

    for _ in range(steps):
        forces = [[0.0, 0.0] for _ in range(count)]

        for i in range(count):
            xi, yi = positions[i]

            for j in range(i + 1, count):
                dx = positions[j][0] - xi
                dy = positions[j][1] - yi
                r2 = dx * dx + dy * dy + softening
                factor = masses[i] * masses[j] / (r2 * math.sqrt(r2))

                fx = factor * dx
                fy = factor * dy
                forces[i][0] += fx
                forces[i][1] += fy
                forces[j][0] -= fx
                forces[j][1] -= fy

        for i in range(count):
            velocities[i][0] += dt * forces[i][0] / masses[i]
            velocities[i][1] += dt * forces[i][1] / masses[i]
            positions[i][0] += dt * velocities[i][0]
            positions[i][1] += dt * velocities[i][1]

    return round(sum(
        x * x + y * y for x, y in positions
    ), 6)

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    output = main(input)
    print(output)