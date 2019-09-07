# https://leetcode.com/problems/word-break/
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
  def wordBreak(self, s, wordDict):  # -> bool
    """
    切分是一种活动，是有步骤的
    固定只能从右往左切
    既然是一维dp，就不再做细致的时间优化了
    """

    @lru_cache(None)
    def dp(i):
      if i == -1:
        return True

      choices = []
      for word in wordDict:
        if s[i - len(word) + 1:i + 1] == word:
          choices.append(dp(i - len(word)))

      return any(choices)

    return dp(len(s) - 1)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().wordBreak(*args), end='\n-----\n')


  test("leetcode", ["leet", "code"])
  test("applepenapple", ["apple", "pen"])
  test("catsandog", ["cats", "dog", "sand", "and", "cat"])

else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
