# https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1057/
import os, sys, re

sys.setrecursionlimit(1000000)
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


def buildTrie(words):
  t = Trie()
  for w in words:
    t.insert(w)
  return t


class Trie:

  def __init__(self):
    self.isWordEnd = False
    self.children = {}

  def insert(self, word: str) -> None:
    if not word:
      self.isWordEnd = True
      return
    firstCh = word[0]
    if firstCh not in self.children:
      self.children[firstCh] = Trie()
    self.children[firstCh].insert(word[1:])

  def search(self, word: str) -> bool:
    if not word:
      return self.isWordEnd
    if word[0] not in self.children:
      return False
    return self.children[word[0]].search(word[1:])

  def startsWith(self, prefix: str) -> bool:
    if not prefix: return True
    if prefix[0] in self.children:
      return self.children[prefix[0]].startsWith(prefix[1:])
    else:
      return False

  def get


class Solution:
  def findMaximumXOR(self, nums):  # -> int
    nums = list(map(lambda n: bin(n)[2:], nums))
    nt = buildTrie(nums)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().findMaximumXOR(*args), end='\n-----\n')


  test()
  test()
else:
  print = lambda *args, **kwargs: None
