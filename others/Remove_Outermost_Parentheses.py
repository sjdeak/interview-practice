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


def removeOutermostParentheses(s):
  matches = re.search(r'^\((.*)\)$', s)
  return matches.group(1)


def splitString(s):
  res = []
  m = 0
  sub = ''
  for i, ch in enumerate(s):
    if ch == '(':
      m += 1
    else:
      m -= 1
    sub += ch
    if not m:
      res.append(sub)
      sub = ''

  return res


class Solution:
  def removeOuterParentheses(self, S):  # -> str
    subs = splitString(S)
    print('subs:', subs)

    return ''.join(map(removeOutermostParentheses, subs))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().removeOuterParentheses(*args), end='\n-----\n')


  test("(()())(())")
  test("(()())(())(()(()))")
  test("()()")
else:
  print = lambda *args, **kwargs: None
