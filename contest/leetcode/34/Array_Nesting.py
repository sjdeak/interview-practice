# https://leetcode.com/contest/leetcode-weekly-contest-34/problems/array-nesting/
import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


# 此题类似连通块染色，因为不需要输出S的具体内容，故直接在nums上染色(各组分别染上了各自的groupId)

def dfs(now, groupId, nums):
  if now == nums[now]:
    return
  nextStep = nums[now]
  nums[now] = groupId
  dfs(nextStep, groupId, nums)


class Solution:
  def arrayNesting(self, nums):  # -> int
    for i, num in enumerate(nums):
      dfs(i, nums[i], nums)
    c = Counter(nums)
    return max(c.values())


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().arrayNesting(*args), end='\n-----\n')


  test([5, 4, 0, 3, 1, 6, 2])
else:
  print = lambda *args, **kwargs: None
