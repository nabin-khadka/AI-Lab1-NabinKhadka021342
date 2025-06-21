import random

x, y = map(int, input("Enter the Size of the Grid (x*y): ").split())
grid = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]

print("Randomly assigned grid states:")
for row in grid:
    print(*row)

pos = [random.randint(0, x - 1), random.randint(0, y - 1)]
print(f"\nInitial Position in the Grid: Room[{pos[0]}, {pos[1]}] => {grid[pos[0]][pos[1]]}")

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
steps = 0

while True:
    if grid[pos[0]][pos[1]] == 1:
        grid[pos[0]][pos[1]] = 0
        print(f"Step {steps + 1}: Room[{pos[0]}, {pos[1]}] was dirty. Cleaned it.")
    else:
        moved = False
        # Goal-based: move to a dirty neighbor if possible
        for dx, dy in directions:
            ni, nj = pos[0] + dx, pos[1] + dy
            if 0 <= ni < x and 0 <= nj < y and grid[ni][nj] == 1:
                pos = [ni, nj]
                print(f"Step {steps + 1}: Current room clean. Moved to dirty neighbor Room[{ni}, {nj}].")
                moved = True
                break
        if not moved:
            found = False
            # If no dirty neighbor, search for any dirty room (goal-directed search)
            for i in range(x):
                for j in range(y):
                    if grid[i][j] == 1:
                        pos = [i, j]
                        print(f"Step {steps + 1}: No dirty neighbor. Moving to Room[{i}, {j}].")
                        found = True
                        break
                if found:
                    break
            if not found:
                print(f"\nAll rooms are clean! Cleaning completed in {steps} steps.")
                break
    steps += 1

print("\nFinal grid state:")
for i in range(x):
    for j in range(y):
        if [i, j] == pos:
            print("P", end=" ")
        else:
            print(grid[i][j], end=" ")
    print()