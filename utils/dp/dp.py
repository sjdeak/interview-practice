from collections import defaultdict


class Solution:
  def coinChange(self, coins, amount):  # -> int
    dp = {}

    for i in range(1):
      pass

    print('dp', dp)
    return dp[-1]


# TLE: O( len(nums) * targetSum )
def package01(nums, targetSum):
  dp = defaultdict(bool)
  length = len(nums)
  for i in range(0, length):
    for s in range(1, targetSum + 1):
      if not i:
        dp[(i, nums[i])] = True
      else:
        dp[(i, s)] = dp[i - 1, s] or dp[i - 1, s - nums[i]]

  print('dp', dp)
  return dp[length - 1, targetSum]


def PackageInfinite(nums, targetSum):
  dp = defaultdict(int)
  length = len(nums)
  for i in range(length):
    for s in range(1, targetSum + 1):
      if not i:
        dp[(0, nums[0])] = 1
        continue

      methodsCnt = 0
      for k in range(s // nums[i]):
        methodsCnt += dp[i - 1, s - k * nums[i]]

  print('dp', dp)
  return dp[length - 1, targetSum]
