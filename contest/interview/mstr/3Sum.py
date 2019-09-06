import sys


def twoSum(arr, st, ed, target):
  res = []

  while st < ed:
    if arr[st] + arr[ed] < target:
      st += 1
    elif arr[st] + arr[ed] > target:
      ed -= 1
    else:
      res.append((arr[st], arr[ed]))
      st += 1
      ed -= 1
  return res


def threeSum(arr, m):
  if len(arr) < 3:
    return []

  ans = []
  arr.sort()
  for i, x in enumerate(arr[:-2]):
    res = twoSum(arr, i + 1, len(arr) - 1, m - x)
    if res:
      for (y, z) in res:
        if len(set([x, y, z])) == 3:
          ans.append(x, y, z)

  return ans
