listA, listB = [], []

with open("./data.txt", "r") as file:
  for line in file:
    a, b = line.strip().split()
    listA.append(int(a))
    listB.append(int(b))

listA.sort()
listB.sort()

diff = 0
for a, b in zip(listA, listB):
  diff += abs(a - b)

print(diff)