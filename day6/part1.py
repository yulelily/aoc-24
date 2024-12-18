grid = []
with open("./data.txt", "r") as file:
  for line in file:
    grid.append(list(line.strip()))

visited = set()
dirs = [[-1,0], [0,1], [1,0], [0,-1]]
def dfs(r: int, c: int, idx: int) -> None:
  while (r in range(rows) and c in range(cols)):
    if grid[r][c] == "#":
      dx, dy = dirs[idx]
      r, c = r-dx, c-dy
      idx = (idx+1) % len(dirs)
    
    visited.add((r, c))
    dx, dy = dirs[idx]
    r, c = r+dx, c+dy


rows, cols = len(grid), len(grid[0])
for r in range(rows):
  for c in range(cols):
    if grid[r][c] == "^":
      dfs(r, c, 0)

print(len(visited))