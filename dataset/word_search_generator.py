# input type: list[str]
import sys
import random
import string

def main(words):
    words = [word.upper() for word in words if word.isalpha()]
    size = max(10, max((len(w) for w in words), default=1) + 2)

    if size > 50:
        raise ValueError("Words must be at most 49 letters long")

    grid = [["." for _ in range(size)] for _ in range(size)]
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    placed = []

    for word in sorted(words, key=len, reverse=True):
        success = False

        for _ in range(500):
            dx, dy = random.choice(directions)
            x = random.randrange(size)
            y = random.randrange(size)
            end_x = x + dx * (len(word) - 1)
            end_y = y + dy * (len(word) - 1)

            if not (0 <= end_x < size and 0 <= end_y < size):
                continue

            cells = [
                (x + dx * i, y + dy * i)
                for i in range(len(word))
            ]

            if all(grid[cy][cx] in (".", word[i])
                   for i, (cx, cy) in enumerate(cells)):
                for i, (cx, cy) in enumerate(cells):
                    grid[cy][cx] = word[i]
                placed.append(word)
                success = True
                break

        if not success:
            placed.append(f"NOT PLACED: {word}")

    for y in range(size):
        for x in range(size):
            if grid[y][x] == ".":
                grid[y][x] = random.choice(string.ascii_uppercase)

    return {
        "grid": "\n".join(" ".join(row) for row in grid),
        "words": placed
    }

if __name__ == "__main__":
    input = sys.argv[1:] if len(sys.argv) > 1 else ["PYTHON", "MACHINE", "LEARN", "PUCKMAN"]
    output = main(input)
    print(output)