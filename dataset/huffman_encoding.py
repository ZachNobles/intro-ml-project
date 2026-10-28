# input type: int
import sys
import heapq
import random

def main(n):
    n = max(1, n)
    rng = random.Random(42)
    alphabet_size = 256
    frequencies = [0] * alphabet_size

    for _ in range(n):
        frequencies[rng.randrange(alphabet_size)] += 1

    heap = [f for f in frequencies if f > 0]
    heapq.heapify(heap)

    if not heap:
        return 0

    total_cost = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = a + b
        total_cost += merged
        heapq.heappush(heap, merged)

    return total_cost

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 5000000
    output = main(input)
    print(output)