# https://www.jisuanke.com/course/804/41863
import unittest
from math import inf


class SegmentTreeMin:
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
    查询[st,ed]的最小值
    """

    def _query(p, l, r, x, y):
      if x <= l and r <= y:
        return self.data[p]

      mid = (l + r) // 2
      res = inf
      if x <= mid:
        res = min(res, _query(p * 2 + 1, l, mid, x, y))
      if y > mid:
        res = min(res, _query(p * 2 + 2, mid + 1, r, x, y))
      return res

    return _query(0, 0, len(self.A) - 1, st, ed)

  def update(self, x, v):
    """
    把第x个结点增加置为v
    """
    self.A[x] = v

    def _update(p, l, r):
      print('p, l, r, x, increment, self.tree:', p, l, r)
      if l == r:
        self.data[p] = v
        return
      mid = (l + r) // 2
      if x <= mid:
        _update(p * 2 + 1, l, mid)
      else:
        _update(p * 2 + 2, mid + 1, r)
      # push child's value up to the parent
      self.data[p] = min(self.data[p * 2 + 1], self.data[p * 2 + 2])

    _update(0, 0, len(self.A) - 1)


class Test(unittest.TestCase):

  def testSum(self):
    t = SegmentTreeMin([1, 2, 3, 4, 5])
    self.assertEqual(min(t.A[:5]), t.query(0, 4))
    t.update(2, 5)
    self.assertEqual(min(t.A[2:4]), t.query(2, 3))
    self.assertEqual(min(t.A[3:5]), t.query(3, 4))
    t.update(1, 8)
    self.assertEqual(min(t.A[:5]), t.query(0, 4))


if __name__ == "__main__":
  # import sys;sys.argv = ['', 'Test.testInit']
  unittest.main()
