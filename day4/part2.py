grid = []
with open("./data.txt", "r") as file:
  for line in file:
    grid.append(list(line.strip()))

rows, cols = len(grid), len(grid[0])
word = "MAS"
res = 0

dirs = [[1,1], [1,-1], [-1,1], [-1,-1]]
def dfs(r: int, c: int, i: int, dx: int, dy: int) -> bool:
  if (r not in range(rows) or
      c not in range(cols) or
      grid[r][c] != word[i]):
      return False
  
  if (i == len(word)-1):
    return True

  return dfs(r+dx, c+dy, i+1, dx, dy)

for r in range(rows):
  for c in range(cols):
    if grid[r][c] == "M":
      for dx, dy in dirs:
        if dfs(r, c, 0, dx, dy) and (dfs(r+2*dx, c, 0, -dx, dy) or dfs(r, c+2*dy, 0, dx, -dy)):
          res += 1

print(res/2)