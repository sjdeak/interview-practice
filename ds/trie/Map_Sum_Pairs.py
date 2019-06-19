# https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1058/
import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


# Trie 插入和查询都用循环实现的版本
class MapSum:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.key, self.value = None, 0
    self.children = {}

  def insert(self, key, val):  # -> None
    now = self
    for ch in key:
      if ch not in now.children:
        now.children[ch] = MapSum()
      now = now.children[ch]

    prefixNode = now
    prefixNode.key, prefixNode.value = key, val

  def sum(self, prefix):  # -> int
    # * getPrefixNode *#
    now = self
    for ch in prefix:
      if ch not in now.children:
        return 0
      now = now.children[ch]

    return self.getSubTreeSum(now)

  def getSubTreeSum(self, now):
    res = now.value
    for child in now.children.values():
      res += self.getSubTreeSum(child)
    return res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  ms = MapSum()
  print('ms.insert("a", 3):', ms.insert("a", 3))
  print('ms.sum("ap"):', ms.sum("ap"))
  print('ms.insert("b", 2):', ms.insert("b", 2))
  print('ms.sum("a"):', ms.sum("a"))

else:
  print = lambda *args, **kwargs: None
