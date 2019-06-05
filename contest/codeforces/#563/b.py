import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  # sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None

if __name__ == '__main__':
  N = int(input())
  A = list(map(int, input().split()))

  oddCnt = len([n for n in A if n % 2])
  if oddCnt == 0 or oddCnt == N:
    print(*A)
  else:
    print(*sorted(A))
