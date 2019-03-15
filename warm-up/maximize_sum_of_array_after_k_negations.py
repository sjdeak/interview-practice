import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter


class Solution:
  def largestSumAfterKNegations(self, A, K: int) -> int:
    A.sort()
    negs = [n for n in A if n < 0] # [-5, -1]
    print('negs', negs)
    N = len(negs)

    res = 0

    if N >= K:
      for i, n in enumerate(A):
        if i < K:
          n = abs(n)
        res += n
    else:
      absA = list(map(lambda n: abs(n), A))
      res = sum(absA)

      left = (K-N)%2
      if left:
        res -= 2*min(absA)

    return res


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  def test(*args):
    print('输入数据: ', *args,
          '\n结果: ', Solution().largestSumAfterKNegations(*args), end='\n-----\n')

  test([4,2,3],1)
  test([3,-1,0,2],3)
  test([2,-3,-1,5,-4],2)
