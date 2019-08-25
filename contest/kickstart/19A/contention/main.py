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
  # sys.stdin = open(os.path.expanduser('./in2.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  from icpc_util import dump_args, debug
else:
  debug = lambda *args, **kwargs: None
  dump_args = lambda func: func


class SegmentTreeSumIntervalSet:
  def __init__(self, A):
    self.length = len(A)

    # 由数组表示的树，下标从0开始
    # 存的是区间和
    self.data = [0] * 4 * self.length
    # lazySet[p] = val:  p指代的区间内的所有项都置为val
    self.lazySet = [0] * 4 * self.length

    # build
    for i, n in enumerate(A):
      self.update(i, n)

  def query(self, st, ed):
    """
    查询[st,ed]的区间和
    """

    def _query(p, l, r, x, y):
      if x <= l <= r <= y:
        return self.data[p]

      self._down(p, l, r)
      mid = (l + r) // 2
      res = 0
      if x <= mid:
        res += _query(p * 2 + 1, l, mid, x, y)
      if y > mid:
        res += _query(p * 2 + 2, mid + 1, r, x, y)
      return res

    return _query(0, 0, self.length - 1, st, ed)

  def update(self, x, v):
    """
    把第x个结点置为v
    """

    def _update(p, l, r):
      # print('[update] p, l, r:', p, l, r)
      if l == r:
        self.data[p] = v
        return
      mid = (l + r) // 2
      if x <= mid:
        _update(p * 2 + 1, l, mid)
      else:
        _update(p * 2 + 2, mid + 1, r)
      # push child's value up to the parent
      self.data[p] = self.data[p * 2 + 1] + self.data[p * 2 + 2]

    _update(0, 0, self.length - 1)

  def _down(self, p, l, r):
    """
    如果p节点有懒标记，就向下执行一层增加
    """
    if self.lazySet[p]:
      mid = (l + r) // 2
      self.data[p * 2 + 1] = self.lazySet[p] * (mid - l + 1)
      self.data[p * 2 + 2] = self.lazySet[p] * (r - (mid + 1) + 1)
      # 分别传递给左右子节点
      self.lazySet[p * 2 + 1] = self.lazySet[p * 2 + 2] = self.lazySet[p]
      # 传递结束
      self.lazySet[p] = 0

  def intervalSet(self, x, y, val):
    """
    把[x,y]内的每一项都置为val
    """

    def _intervalSet(p, l, r):
      # print('[intervalSet] p, l, r, x, y, val:', p, l, r, x, y, val)
      # print('self.data:', self.data)

      if x <= l <= r <= y:  # p指向[l,r]区间，[l,r]被[x,y]完整包含，不需要再修改子节点
        self.data[p] = (r - l + 1) * val
        self.lazySet[p] = val  # 增加标记，表示子结点还没有被修改
        return  # 不需要再往下前进 因为[l,r]被[x,y]完整包含

      self._down(p, l, r)
      mid = (l + r) // 2
      if x <= mid:
        _intervalSet(p * 2 + 1, l, mid)
      if y > mid:
        _intervalSet(p * 2 + 2, mid + 1, r)
      # push up child's value
      self.data[p] = self.data[p * 2 + 1] + self.data[p * 2 + 2]

    _intervalSet(0, 0, self.length - 1)


# WA 区间间的先后不代表大小  两个区间不相交不代表这两个区间等价
def cmp(a, b):
  na, nb = sorted([a, b])
  lenA, lenB = na.r - na.l + 1, nb.r - nb.l + 1
  if na.r < nb.l:  # 两个区间不相交
    left = min(lenA, lenB)
    right = min(lenA, lenB)
  elif na.l <= nb.l <= nb.r <= na.r:  # na包含nb
    left = 0  # na 在前
    right = min(lenB, lenA - lenB)  # nb在前
  else:  # 相交
    left = min(lenA, lenB - (na.r - nb.l + 1))
    right = min(lenB, lenA - (na.r - nb.l + 1))

  if left < right:
    res = 1  # a negative number for less-than
  elif left > right:
    res = -1  # a positive number for greater-than
  else:
    res = 0  # zero for equality
  debug('na, nb, left, right:', na, nb, left, right)
  res = res if na == a else -res
  # debug('a, b, res:', a, b, res)
  return res


if __name__ == '__main__':
  T = int(input())
  for caseIndex in range(T):
    N, Q = list(map(int, input().split()))
    Books = [namedtuple('book', ['l', 'r'])(*map(lambda s: int(s) - 1, input().split())) for i in range(Q)]
    debug('Books (Raw):', Books)
    Books.sort(key=cmp_to_key(cmp))
    debug('Books (Sorted):', Books)

    tr = SegmentTreeSumIntervalSet([0] * N)
    ans = inf
    for b in Books:
      before = tr.query(b.l, b.r)
      tr.intervalSet(b.l, b.r, 1)
      after = tr.query(b.l, b.r)
      ans = min(ans, after - before)

    print('Case #{}: {}'.format(caseIndex + 1, ans))
