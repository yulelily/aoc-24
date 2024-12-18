from collections import defaultdict

rules, updates = defaultdict(list), []
emptyline = False
with open("./data.txt", "r") as file:
  for line in file:
    if line == "\n":
      emptyline = True
      continue

    if emptyline:
      updates.append(line.strip().split(","))
    else:
      x, y = line.strip().split("|")
      rules[x].append(y)

res = 0
for update in updates:
  prevRules = set()
  correct = True
  for n in reversed(update):
    if n in prevRules:
      correct = False
      break
    
    prevRules.update(rules[n])

  if correct:
    res += int(update[len(update)//2])

print(res)