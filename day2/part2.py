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
    
    i = check(nums)
    if i == -1 or check(nums[1:]) == -1 or check(nums[:i] + nums[i+1:]) == -1 or check(nums[:i+1] + nums[i+2:]) == -1:
      reports += 1
    
print(f"reports: {reports}")