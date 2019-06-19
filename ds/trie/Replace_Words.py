# https://leetcode.com/problems/replace-words/
import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right

"""
改造Trie
1. 增加保存信息
2. 返回某一前缀下的所有串及其额外信息
"""


class Trie:

  def __init__(self):
    self.data = ''
    self.isWordEnd = False
    self.children = {}

  def insert(self, word, rawWord) -> None:
    if not word:
      self.data = rawWord
      self.isWordEnd = True
      return
    firstCh = word[0]
    if firstCh not in self.children:
      self.children[firstCh] = Trie()
    self.children[firstCh].insert(word[1:], rawWord)

  def search(self, word: str) -> bool:
    if not word:
      return self.isWordEnd
    if word[0] not in self.children:
      return False
    return self.children[word[0]].search(word[1:])

  def getPrefixNode(self, prefix: str):
    """
    找到时返回prefix最后一个字符所在的Trie节点
    找不到时返回False
    """
    if not prefix: return self
    if prefix[0] in self.children:
      return self.children[prefix[0]].getPrefixNode(prefix[1:])
    else:
      return False

  def getShortestPrefixOf(self, word):
    """
    在Trie中寻找 word 的最短前缀
    找不到时返回False
    """
    if self.isWordEnd:
      return self.data
    if not word or word[0] not in self.children:
      return False
    return self.children[word[0]].getShortestPrefixOf(word[1:])


# 题目数据很弱
class Solution:
  def replaceWords(self, dict, sentence):  # -> str
    dictTrie = Trie()
    for i, w in enumerate(dict):
      dictTrie.insert(w, i + 1)  # 这里把所有的下标加了1   不然返回下标0时无法和返回False时区分
    idxs = []
    sentence = sentence.split()
    for w in sentence:
      shortestPrefix = dictTrie.getShortestPrefixOf(w)

      print('w, shortestPrefix:', w, shortestPrefix)

      if shortestPrefix:
        idxs.append(shortestPrefix)
      else:
        idxs.append(-1)

    ans = []
    for i, idx in enumerate(idxs):
      if idx == -1:
        ans.append(sentence[i])
      else:
        ans.append(dict[idx - 1])  # 再把下标减回去

    return ' '.join(ans)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().replaceWords(*args), end='\n-----\n')


  test(["cat", "bat", "rat"], "the cattle was rattled by the battery")
  # test()
else:
  print = lambda *args, **kwargs: None
