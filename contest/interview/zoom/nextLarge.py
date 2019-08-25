import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy

sys.setrecursionlimit(1000000)


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  # sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


# WA
def nextLarge(n):
  digits = list(map(int, str(n)))
  if len(digits) == 1:
    return -1
  ans = inf
  for i, digit in enumerate(digits[:-1]):
    if not digits[i] < digits[i + 1]:
      continue

    choice = digits[:i + 2]
    tmp = choice[i + 1]
    choice[i + 1] = choice[i]
    choice[i] = tmp

    digitLeft = digits[i + 2:]
    digitLeft.sort()
    print('digits, choice, digitLeft:', digits, choice, digitLeft)
    choice += digitLeft

    res = int(''.join(map(str, choice)))
    ans = min(ans, res)

  return ans if ans != inf else -1


if __name__ == '__main__':
  print('nextLarge(218765):', nextLarge(218765))
  print('nextLarge(1234):', nextLarge(1234))
  print('nextLarge(4321):', nextLarge(4321))
  print('nextLarge(534976):', nextLarge(534976))
