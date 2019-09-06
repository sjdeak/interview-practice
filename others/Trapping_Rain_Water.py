# https://leetcode.com/problems/trapping-rain-water/
import os
import sys
from math import inf

sys.setrecursionlimit(1000000)


# 🗳 A[:i]的前缀和
def getPrefixSum(A):
  res = [0]
  for i in range(len(A)):
    res.append(A[i] + res[i])
  return res


class Solution:
  def trap(self, A):  # -> int
    i = 0
    ans = 0
    ps = getPrefixSum(A)
    while i != len(A) - 2:
      while A[i] == 0:
        i += 1
      j = i + 1
      midMin = inf  # (i,j)间的最小值
      while midMin > min(A[i], A[j]):
        midMin = min(midMin, A[j])
        j += 1
      print('i,j:', i, j)
      ans += (j - i) + 1 * min(A[i], A[j]) - (ps[j] - ps[i + 1])
      i = j

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().trap(*args), end='\n-----\n')


  test([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
  # test()
else:
  print = lambda *args, **kwargs: None
