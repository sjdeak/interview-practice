# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
import os


def refreshGlobals():
  pass


refreshGlobals()


# The isBadVersion API is already defined for you.
#  version, an integer
#  a bool
# def isBadVersion(version):

# 🗳 lower_bound
# A: "GGGBBBB"   且保证有解
class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 1, n
    while left < right:
      mid = left + (right - left) // 2
      if isBadVersion(mid):
        right = mid
      else:
        left = mid + 1

    return left


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().firstBadVersion(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
