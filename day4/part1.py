grid = []
with open("./data.txt", "r") as file:
  for line in file:
    grid.append(list(line.strip()))

rows, cols = len(grid), len(grid[0])
word = "XMAS"
res = [0]

dirs = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
def dfs(r: int, c: int, i: int, dx: int, dy: int) -> None:
  if (r not in range(rows) or
      c not in range(cols) or
      grid[r][c] != word[i]):
      return
  
  if (i == len(word)-1):
    res[0] += 1
    return

  dfs(r+dx, c+dy, i+1, dx, dy)

for r in range(rows):
  for c in range(cols):
    if grid[r][c] == "X":
      for dx, dy in dirs:
        dfs(r, c, 0, dx, dy)

print(res[0])