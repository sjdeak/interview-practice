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
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


class SegmentTree:
  def __init__(self, A):
    self.A = [0] * len(A)

    # 由数组表示的树，下标从0开始
    # 存的是区间和
    self.data = [0] * 4 * len(A)

    # build
    for i, n in enumerate(A):
      self.update(i, n)

  def query(self, st, ed):
    """
    查询[st,ed]的xor-sum
    """

    def _query(p, l, r, x, y):
      if x <= l and r <= y:
        return self.data[p]

      mid = (l + r) // 2
      res = 0
      if x <= mid:
        res ^= _query(p * 2 + 1, l, mid, x, y)
      if y > mid:
        res ^= _query(p * 2 + 2, mid + 1, r, x, y)
      return res

    return _query(0, 0, len(self.A) - 1, st, ed)

  def update(self, x, v):
    """
    把第x个结点增加置为v
    """
    self.A[x] = v

    def _update(p, l, r):
      # print('p, l, r, x, increment, self.tree:', p, l, r)
      if l == r:
        self.data[p] = v
        return
      mid = (l + r) // 2
      if x <= mid:
        _update(p * 2 + 1, l, mid)
      else:
        _update(p * 2 + 2, mid + 1, r)
      # push child's value up to the parent
      self.data[p] = self.data[p * 2 + 1] ^ self.data[p * 2 + 2]

    _update(0, 0, len(self.A) - 1)


def isXOREven(n):
  return Counter(bin(n)[2:])['1'] % 2 == 0


# @dump_args
def getLargestSubInterval(left, right):
  if left == right:
    return int(isXOREven(st.query(left, right)))

  mid = left + (right - left) // 2

  leftRes = getLargestSubInterval(left, mid)
  rightRes = getLargestSubInterval(mid + 1, right)

  midRes = 0
  if isXOREven(st.query(mid, mid)):
    for j in range(mid, left - 1, -1):
      if isXOREven(st.query(j, mid)):
        midRes += 1
      else:
        break
    for j in range(mid + 1, right + 1):
      if isXOREven(st.query(mid, j)):
        midRes += 1
      else:
        break
  # print('midRes:', midRes)

  # debug('left, right, leftRes, midRes, rightRes:', left, right, leftRes, midRes, rightRes)
  return max(leftRes, midRes, rightRes)


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    st = SegmentTree(A)
    ans = []
    for _ in range(Q):
      P, V = list(map(int, input().split()))
      st.update(P, V)
      # debug('st.A:', st.A)
      ans.append(getLargestSubInterval(0, N - 1))

    print('Case #{}:'.format(caseIndex + 1), *ans)
