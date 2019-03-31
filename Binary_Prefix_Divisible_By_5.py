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
  def prefixesDivBy5(self, A):  # -> List[bool]
    length = len(A)
    for i in range(1, length):
      A[i] = A[i - 1] * 2 + A[i]

    return list(map(lambda n: not (n % 5), A))


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().prefixesDivBy5(*args), end='\n-----\n')


  test([0, 1, 1])
  test([1, 1, 1])
  test([0, 1, 1, 1, 1, 1])
  test([1, 1, 1, 0, 1])
