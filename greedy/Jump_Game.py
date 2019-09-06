# https://leetcode.com/problems/jump-game/
import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy

sys.setrecursionlimit(1000000)


class Solution:
  def canJump(self, nums):  # -> bool
    print('nums:', nums)
    if len(nums) == 1:
      return True
    for k in range(1, nums[0] + 1):
      if self.canJump(nums[k:]):
        return True
    return False


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().canJump(*args), end='\n-----\n')


  test([2, 3, 1, 1, 4])
  # test([3,2,1,0,4])
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
