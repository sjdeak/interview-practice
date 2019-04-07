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


class Solution:
  def videoStitching(self, clips, T):  # -> int
    clips.sort(key=itemgetter(0))
    length = len(clips)
    cur = 0
    vis = set()
    ans = 0
    while cur < T:
      print('cur, T:', cur, T)
      choices = [(i, clips[i][0], clips[i][1]) for i in range(length)
                 if clips[i][0] <= cur and i not in vis]
      if not choices:
        return -1
      chosen = max(choices, key=itemgetter(2))
      print('choices, chosen:', choices, chosen)
      ans += 1
      cur = chosen[2]
      vis.add(chosen[0])

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().videoStitching(*args), end='\n-----\n')


  test([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10)
  test([[0, 1], [1, 2]], 5)
  test([[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5],
        [5, 7], [6, 9]], 9)
  test([[0, 4], [2, 8]], 5)
else:
  print = lambda *args, **kwargs: None
