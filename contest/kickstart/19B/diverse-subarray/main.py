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


# template SegmentTreeMaxSum
class SegmentTreeMaxSum:
  def __init__(self, A):
    self.A = [0] * len(A)

    # 由数组表示的树，下标从0开始

    self.sumData = [0] * 4 * len(A)  # 区间和
    self.maxSumData = [0] * 4 * len(A)  # 最大区间和

    # build
    for i, n in enumerate(A):
      self.update(i, n)

  def query(self, st, ed):
    """
    查询[st,ed]的区间和
    """

    def _query(p, l, r, x, y):
      if x <= l and r <= y:
        return self.maxSumData[p]

      mid = (l + r) // 2
      res = 0
      if x <= mid:
        res += _query(p * 2 + 1, l, mid, x, y)
      if y > mid:
        res += _query(p * 2 + 2, mid + 1, r, x, y)
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
        self.sumData[p] = self.maxSumData[p] = v
        return
      mid = (l + r) // 2
      if x <= mid:
        _update(p * 2 + 1, l, mid)
      else:
        _update(p * 2 + 2, mid + 1, r)
      # push child's value up to the parent
      self.sumData[p] = self.sumData[p * 2 + 1] + self.sumData[p * 2 + 2]
      # max(没有延伸至右半区间的区间中的最大区间和, 延伸至右半区间的区间中的最大区间和)
      self.maxSumData[p] = max(self.maxSumData[p * 2 + 1], self.sumData[p * 2 + 1] + self.maxSumData[p * 2 + 2])

    _update(0, 0, len(self.A) - 1)


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))
    effector = A.copy()
    counter = defaultdict(int)
    watershed = defaultdict(list)
    watershedBeginAt = defaultdict(int)

    for i, n in enumerate(A):
      counter[n] += 1
      if counter[n] <= S:
        effector[i] = 1
      elif counter[n] == S + 1:
        effector[i] = -S
        watershed[n].append(i)
      else:
        effector[i] = 0
        watershed[n].append(i)

    debug('effector:', effector)
    debug('watershed:', watershed)

    tr = SegmentTreeMaxSum(effector)
    ans = tr.query(0, len(effector) - 1)
    for k in range(N - 1):  # 从k之后开始选
      n = A[k]
      tr.update(k, 0)
      if len(watershed[n]) - 1 >= watershedBeginAt[n]:
        tr.update(watershed[n][watershedBeginAt[n]], 1)
        watershedBeginAt[n] += 1
      if len(watershed[n]) - 1 >= watershedBeginAt[n]:
        tr.update(watershed[n][watershedBeginAt[n]], -S)
      debug('k, tr.A:', k, tr.A)
      ans = max(ans, tr.query(0, len(effector) - 1))

    print('Case #{}: {}'.format(caseIndex + 1, ans))
