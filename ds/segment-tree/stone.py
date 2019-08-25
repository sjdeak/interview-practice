# 黑白石头 https://www.jisuanke.com/course/804/41868
import unittest


class SegmentTreeIntervalSet:
  def __init__(self, A):
    self.length = len(A)

    # 由数组表示的树，下标从0开始
    # 存的是区间内最长的连续1的个数
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
      print('[update] p, l, r:', p, l, r)
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

  def intervalToggle(self, x, y):

    def _toggle(p, l, r):
      print('[intervalToggle] p, l, r, x, y, val:', p, l, r, x, y)
      print('self.data:', self.data)

      if x <= l <= r <= y:  # p指向[l,r]区间，[l,r]被[x,y]完整包含，不需要再修改子节点
        self.data[p] = (r - l + 1) * val
        self.lazySet[p] = val  # 增加标记，表示子结点还没有被修改
        return  # 不需要再往下前进 因为[l,r]被[x,y]完整包含

      self._down(p, l, r)
      mid = (l + r) // 2
      if x <= mid:
        _toggle(p * 2 + 1, l, mid)
      if y > mid:
        _toggle(p * 2 + 2, mid + 1, r)
      # push up child's value
      self.data[p] = self.data[p * 2 + 1] + self.data[p * 2 + 2]

    _toggle(0, 0, self.length - 1)


class Test(unittest.TestCase):

  def testSum(self):
    # 测试数据来自 帕吉的肉钩 https://www.jisuanke.com/course/804/41866

    t = SegmentTreeIntervalSet([1, 0, 1, 0])
    self.assertEqual(1, t.query(0, 3))
    t.intervalToggle(1, 2)
    self.assertEqual(2, t.query(0, 3))
    t.intervalToggle(2, 2)
    self.assertEqual(0, t.query(3, 3))

    # self.assertEqual(t.query(0, 9), 25)

    # self.assertEqual(t.query(0, 1), 4)

    # t.update(0, 100)
    # self.assertEqual(t.query(0,1), 102)


if __name__ == "__main__":
  # import sys;sys.argv = ['', 'Test.testInit']
  unittest.main()
"""
  # t = SegmentTreeSum([1] * 10)
  # t.intervalAdd(0, 4, 1)
  
  t = SegmentTreeSumIntervalAdd([1] * 10)
  # t.intervalAdd(0, 4, 1)  # [2,2,2,2,2,1,1,1,1,1]
  t.intervalSet(4, 8, 3)  # [1,1,1,1,3,3,3,3,3,1]

  # self.assertEqual(t.query(0, 9), 25)
  print('t.data:', t.data)
  print('t.query(0, 9):', t.query(0, 9))
  print('t.lazySet:', t.lazySet)
"""
