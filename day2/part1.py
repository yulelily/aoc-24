from typing import List

def check(nums: List[int]) -> int:
  slope = -1 if nums[0] < nums[1] else 1

  for i in range(0, len(nums)-1):
    if not (1 <= slope * (nums[i] - nums[i+1]) <= 3):
      return i
    
  return -1

reports = 0
with open ("./data.txt", "r") as file:
  for line in file:
    nums = [int(x) for x in line.strip().split()]
    slope = -1 if nums[0] - nums[1] < 0 else 1

    if check(nums) == -1:
      reports += 1

print(reports)