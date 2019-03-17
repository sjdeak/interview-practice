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
  def bitwiseComplement(self, N: int) -> int:
    b = bin(N)[2:]
    b = b.translate(str.maketrans('01', '10'))
    return int(b, 2)


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  def test(*args):
    print('输入数据: ', *args,
          '\n结果: ', Solution().bitwiseComplement(*args), end='\n-----\n')

  test(5)
  test(7)
  test(10)
  test(0)
