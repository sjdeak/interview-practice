import os
import sys
from functools import cmp_to_key
from math import inf


class CustomException(Exception): pass


if os.getenv('SJDEAK'):
  sys.stdin = open(os.path.expanduser('./in.txt'))
  # sys.stdout = open(os.path.expanduser('./out.txt'), 'w')
  debug = print
else:
  debug = lambda *args, **kwargs: None


class SegmentTreeMaxExtended:
  def __init__(self, A):
    self.A = [0] * len(A)

    # 由数组表示的树，下标从0开始
    # 存的是区间和
    self.dataMaxVal = [0] * 4 * len(A)
    self.dataIndex = [0] * 4 * len(A)

    # build
    for i, n in enumerate(A):
      self.update(i, n)

  def query(self, st, ed):
    """
    查询[st,ed]的最大值
    """

    def _query(p, l, r, x, y):
      if x <= l and r <= y:
        return self.dataMaxVal[p]

      mid = (l + r) // 2
      res = -inf
      if x <= mid:
        res = max(res, _query(p * 2 + 1, l, mid, x, y))
      if y > mid:
        res = max(res, _query(p * 2 + 2, mid + 1, r, x, y))
      return res

    return _query(0, 0, len(self.A) - 1, st, ed)

  def queryIndex(self, st, ed):
    """
    查询[st,ed]内最大值的下标
    """

    def cmp(i1, i2):
      if self.A[i1] != self.A[i2]:
        return self.A[i1] < self.A[i2]
      else:
        return i1 <= i2

    def _query(p, l, r, x, y):
      if x <= l and r <= y:
        return self.dataIndex[p]

      mid = (l + r) // 2
      choices = []
      if x <= mid:
        choices.append(_query(p * 2 + 1, l, mid, x, y))
      if y > mid:
        choices.append(_query(p * 2 + 2, mid + 1, r, x, y))
      return max(choices, key=cmp_to_key(cmp))

    return _query(0, 0, len(self.A) - 1, st, ed)

  def update(self, x, v):
    """
    把第x个结点增加置为v
    """
    self.A[x] = v

    def _update(p, l, r):
      # print('p, l, r, x, increment, self.tree:', p, l, r)
      if l == r:
        self.dataMaxVal[p] = v
        self.dataIndex[p] = l
        return
      mid = (l + r) // 2
      if x <= mid:
        _update(p * 2 + 1, l, mid)
      else:
        _update(p * 2 + 2, mid + 1, r)

      # push child's value up to the parent
      if self.dataMaxVal[p * 2 + 1] >= self.dataMaxVal[p * 2 + 2]:
        self.dataMaxVal[p] = self.dataMaxVal[p * 2 + 1]
        self.dataIndex[p] = self.dataIndex[p * 2 + 1]
      else:
        self.dataMaxVal[p] = self.dataMaxVal[p * 2 + 2]
        self.dataIndex[p] = self.dataIndex[p * 2 + 2]

    _update(0, 0, len(self.A) - 1)


if __name__ == '__main__':
  H, W, N = list(map(int, input().split()))
  widths = [int(input()) for i in range(N)]
  t = SegmentTreeMaxExtended([W] * H)

  for w in widths:
    i = t.queryIndex(0, W - 1)
    print('w, t.A, i:', w, t.A, i)
    if t.A[i] >= w:
      t.update(i, t.A[i] - w)
      print(i + 1)
    else:
      print(-1)
