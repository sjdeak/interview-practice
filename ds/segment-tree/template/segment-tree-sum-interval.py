import unittest


class SegmentTreeSum:
  def __init__(self, A):
    self.length = len(A)

    # 由数组表示的树，下标从0开始
    # 存的是区间和
    self.data = [0] * 4 * self.length
    # lazyInc[p] = xxx:  p指代的区间内的项需要全部增加xxx
    self.lazyInc = [0] * 4 * self.length

    # build
    for i, n in enumerate(A):
      self.update(i, n)

  def query(self, st, ed):
    """
    查询[st,ed]的区间和
    """

    def _query(p, l, r, x, y):
      if x <= l and r <= y:
        return self.data[p]

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
      self.data[p] = self.data[p * 2 + 1] + self.data[p * 2 + 2]

    _update(0, 0, self.length - 1)

  def _down(self, p, l, r):
    """
    把p节点的懒修改向下执行一层
    """
    if self.lazyInc[p]:
      mid = l + (r - l) // 2
      self.data[p * 2 + 1] += self.lazyInc[p] * (mid - l + 1)
      self.data[p * 2 + 2] += self.lazyInc[p] * (r - (mid + 1) + 1)
      self.lazyInc[p * 2 + 1] += self.lazyInc[p]
      self.lazyInc[p * 2 + 2] += self.lazyInc[p]
      self.lazyInc[p] = 0

  def intervalIncrease(self, x, y, increment):
    """
    把[x,y]内的每一项都增加increment
    """

    def _update(p, l, r):
      print('p, l, r, x, increment, self.tree:', p, l, r)
      if l == r:
        self.data[p] += increment
        return
      mid = (l + r) // 2
      if x <= mid:
        _update(p * 2 + 1, l, mid)
      else:
        _update(p * 2 + 2, mid + 1, r)
      # push child's value up to the parent
      self.data[p] = self.data[p * 2 + 1] + self.data[p * 2 + 2]

    _update(0, 0, self.length - 1)

  def intervalSetValue(self, x, y, v):
    """
    把[x,y]内的每一项都置为v
    """
    pass


class Test(unittest.TestCase):

  def testSum(self):
    t = SegmentTreeSum([8, 7, 3, 9, 5, 1, 10])

    self.assertEqual(sum(t.A[1:4]), t.query(1, 3))
    self.assertEqual(sum(t.A), t.query(0, 6))

    t.update(3, 2)
    self.assertEqual(sum(t.A[1:4]), t.query(1, 3))
    t.update(2, 1)
    self.assertEqual(sum(t.A[1:4]), t.query(1, 3))


if __name__ == "__main__":
  # import sys;sys.argv = ['', 'Test.testInit']
  unittest.main()
