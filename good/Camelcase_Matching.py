import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter
from queue import Queue


def refreshGlobals():
  pass


refreshGlobals()


# 从q[st:]里找ch
def check(s, ch):
  if ch.isupper():
    for i in range(len(s)):
      if s[i].isupper():
        return i if s[i] == ch else None
      else:
        continue
    return None
  else:  # ch 为小写
    for i in range(len(s)):
      if s[i].isupper():
        return None
      else:
        if s[i] != ch:
          continue
        else:
          return i
    return None


def solve(q, p):
  nextIndex = 0
  for i, ch in enumerate(p):
    res = check(q[nextIndex:], ch)
    print('q[nextIndex:]:', q[nextIndex:], 'ch:', ch, 'res:', res)
    if res is not None:
      nextIndex += res + 1
    else:
      return False
  print('q, nextIndex:', q, nextIndex)
  print('q[nextIndex:]:', q[nextIndex:])
  return all(map(lambda ch: ch.islower(), q[nextIndex:]))


class Solution:
  def camelMatch(self, queries, pattern):  # -> List[bool]
    return list(map(lambda q: solve(q, pattern), queries))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().camelMatch(*args), end='\n-----\n')


  test(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB")
  test(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa")
  test(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT")
else:
  print = lambda *args, **kwargs: None
