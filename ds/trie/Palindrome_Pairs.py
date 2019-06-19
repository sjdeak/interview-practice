# https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1138/
import os, sys, re
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1000000)

"""
扩展后的Trie
1. 增加保存信息
2. 返回某一前缀下的所有串及其额外信息
"""


class Trie:

  def __init__(self):
    self.data = ''
    self.isWordEnd = False
    self.children = {}

  def insert(self, word, data) -> None:
    if not word:
      self.data = data
      self.isWordEnd = True
      return
    firstCh = word[0]
    if firstCh not in self.children:
      self.children[firstCh] = Trie()
    self.children[firstCh].insert(word[1:], data)

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

  def getAllChildNode(self, node, isRoot):
    """
    返回Trie中node及node的所有字节点
    :param node:
    :param isRoot: 是否是第一次调用(根调用)
    :rtype [Trie]
    """
    if node.isWordEnd and not isRoot:
      return [node]

    res = []
    if node.isWordEnd and isRoot:
      res = [node]
    for ch in node.children:
      res += self.getAllChildNode(node.children[ch], False)
    return res

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


def isPalindromic(s):
  return s == s[::-1]


class Solution:
  def palindromePairs(self, words):  # -> List[List[int]]
    self.wordsTrie = Trie()
    self.idxMap = {}
    # * 建立wordsTrie, 节点data里保存在words里的下标 *#
    for i, w in enumerate(words):
      self.wordsTrie.insert(w, w)
      self.idxMap[w] = i

    # * words 从短串到长串 逐个检查 *#
    words.sort(key=len)
    self.ans = []
    for w in words:
      self.findPairs(w)

    return self.ans

  def findPairs(self, w):
    prefixEndNode = self.wordsTrie.getPrefixNode(w[::-1])
    if prefixEndNode:
      res = self.wordsTrie.getAllChildNode(prefixEndNode, True)
      print('w, rawRes:', w, list(map(lambda n: n.data, res)))
      res = list(filter(lambda s: s != w and len(w) <= len(s) and isPalindromic(s[len(w):]),
                        map(lambda n: n.data, res)))
      print('w, finalRes:', w, list(res))
      for r in res:
        self.ans.append([self.idxMap[w], self.idxMap[r]])

  # def findWordWithPalindromeA2(self, node, now):
  #   res = []
  #   if node.isWordEnd and now and isPalindrome(now):
  #     return [node.data]
  #   for ch in node.children:
  #     res += self.findWordWithPalindromeA2(node.children[ch], now+ch)
  #   return res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().palindromePairs(*args), end='\n-----\n')


  test(["abcd", "dcba", "lls", "s", "sssll"])
  test(["bat", "tab", "cat"])
else:
  print = lambda *args, **kwargs: None
