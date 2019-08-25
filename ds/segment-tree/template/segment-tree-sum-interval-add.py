import unittest


# template SegmentTreeSumIntervalAdd
class SegmentTreeSumIntervalAdd:
  def __init__(self, A):
    self.length = len(A)

    # 由数组表示的树，下标从0开始
    # 存的是区间和
    self.data = [0] * 4 * self.length
    # lazyInc[p] = val:  p指代的区间内的所有项都增加val
    self.lazyAdd = [0] * 4 * self.length

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
      print('[update] p, l, r, x, increment, self.tree:', p, l, r)
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
    if self.lazyAdd[p]:
      mid = l + (r - l) // 2
      self.data[p * 2 + 1] += self.lazyAdd[p] * (mid - l + 1)
      self.data[p * 2 + 2] += self.lazyAdd[p] * (r - (mid + 1) + 1)
      # 分别传递给左右子节点
      self.lazyAdd[p * 2 + 1] += self.lazyAdd[p]
      self.lazyAdd[p * 2 + 2] += self.lazyAdd[p]
      # 传递结束
      self.lazyAdd[p] = 0

  def intervalAdd(self, x, y, inc):
    """
    把[x,y]内的每一项都增加inc
    """

    def _update(p, l, r):
      print('[intervalAdd] p, l, r, x, y, increment:', p, l, r, x, y, inc)

      if x <= l <= r <= y:  # p指向[l,r]区间，[l,r]完整被[x,y]包含，不需要再修改子节点
        self.data[p] += (r - l + 1) * inc
        self.lazyAdd[p] += inc  # 增加标记，表示子结点还没有被修改
        return  # 不需要再往下前进

      self._down(p, l, r)
      mid = (l + r) // 2
      if x <= mid:
        _update(p * 2 + 1, l, mid)
      if y > mid:
        _update(p * 2 + 2, mid + 1, r)
      # push up child's value
      self.data[p] = self.data[p * 2 + 1] + self.data[p * 2 + 2]

    _update(0, 0, self.length - 1)



class Test(unittest.TestCase):

  def testSum(self):
    # 测试数据来自 区间整数操作 https://www.jisuanke.com/course/804/41867
    t = SegmentTreeSumIntervalAdd(list(range(1, 11)))
    self.assertEqual(4, t.query(3, 3))
    self.assertEqual(55, t.query(0, 9))
    self.assertEqual(9, t.query(1, 3))
    t.intervalAdd(2, 5, 3)
    self.assertEqual(15, t.query(1, 3))

    """
    t = SegmentTreeSumIntervalAdd([1] * 10)
    t.intervalAdd(0, 4, 1)  # [2,2,2,2,2,1,1,1,1,1]
    # t.intervalSet(4, 8, 2)  # [2,2,2,2,4,3,3,3,3,1]

    # self.assertEqual(t.query(0, 9), 25)
    self.assertEqual(t.query(0, 9), 15)
    self.assertEqual(t.query(0, 1), 4)

    # t.update(0, 100)
    # self.assertEqual(t.query(0,1), 102)
    """

if __name__ == "__main__":
  # import sys;sys.argv = ['', 'Test.testInit']
  unittest.main()

  # t = SegmentTreeSum([1] * 10)
  # t.intervalAdd(0, 4, 1)
