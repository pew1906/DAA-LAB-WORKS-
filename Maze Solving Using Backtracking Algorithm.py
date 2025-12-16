# Assignment 07: Maze Solving Using Backtracking Algorithm
import matplotlib.pyplot as plt
import time

maze = [
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1]
]

N = len(maze)

solution = [[0] * N for _ in range(N)]

def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1

def show_board(title=""):
    cmap = plt.cm.colors.ListedColormap(["white", "green", "red"])
    plt.imshow(solution, cmap=cmap, origin="upper", vmin=0, vmax=2)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.pause(0.35)
    plt.clf()

def solve_maze(x, y):
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        solution[x][y] = 1
        show_board("Goal reached!")
        return True

    if is_safe(x, y) and solution[x][y] == 0:
        solution[x][y] = 1
        show_board(f"Visiting ({x},{y})")

        if solve_maze(x, y + 1): return True   # right
        if solve_maze(x + 1, y): return True   # down
        if solve_maze(x, y - 1): return True   # left
        if solve_maze(x - 1, y): return True   # up

        solution[x][y] = 2
        show_board(f"Backtracking from ({x},{y})")
        return False

    return False

plt.figure(figsize=(6, 6))
if solve_maze(0, 0):
    print("Path found!")
else:
    print("No path exists.")
plt.close()
