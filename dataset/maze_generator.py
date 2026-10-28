# input type: int
import sys
import random

def main(size):
    if not 2 <= size <= 30:
        raise ValueError("Size must be between 2 and 30")

    width = size * 2 + 1
    height = size * 2 + 1
    maze = [["#"] * width for _ in range(height)]
    visited = set()
    stack = [(1, 1)]
    maze[1][1] = " "
    visited.add((1, 1))

    while stack:
        x, y = stack[-1]
        neighbors = []

        for dx, dy in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if (nx, ny) not in visited:
                    neighbors.append((nx, ny, dx, dy))

        if neighbors:
            nx, ny, dx, dy = random.choice(neighbors)
            maze[y + dy // 2][x + dx // 2] = " "
            maze[ny][nx] = " "
            visited.add((nx, ny))
            stack.append((nx, ny))
        else:
            stack.pop()

    maze[1][1] = "S"
    maze[height - 2][width - 2] = "E"

    return "\n".join("".join(row) for row in maze)

if __name__ == "__main__":
    input = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    output = main(input)
    print(output)