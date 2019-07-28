# https://leetcode.com/problems/container-with-most-water/solution/
import os
import sys
from math import inf

sys.setrecursionlimit(1000000)


class Solution:
  def maxArea(self, A):  # -> int
    pl, pr = 0, len(A) - 1
    ans = -inf
    while pl < pr:
      print('pl, pr, A[pl], A[pr]:', pl, pr, A[pl], A[pr])
      ans = max(ans, min(A[pl], A[pr]) * (pr - pl))
      if A[pl] >= A[pr]:
        pr -= 1
      else:
        pl += 1

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxArea(*args), end='\n-----\n')


  test([1, 8, 6, 2, 5, 4, 8, 3, 7])
  test([1, 2])
  test([2, 3, 4, 5, 18, 17, 6])
else:
  print = lambda *args, **kwargs: None
