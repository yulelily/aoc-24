listA, listB = [], []

with open("./data.txt", "r") as file:
  for line in file:
    a, b = line.strip().split()
    listA.append(int(a))
    listB.append(int(b))

simScore = 0
count = {}
for b in listB:
  count[b] = count.get(b, 0) + 1

for a in listA:
  if a in count:
    simScore += a * count[a]

print(simScore)