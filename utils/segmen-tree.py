getLeftNodeIndex = lambda i: 2 * i + 1
getRightNodeIndex = lambda i: 2 * i + 2


class RMQSegmentTree:
  def __init__(self, arr):
    length = len(arr)
    self.arr = arr

    # 由数组表示的树，下标从0开始
    # 存的是区间内的最小值，而非最小值的下标
    self.rmqTree = [0] * 4 * length

    self.build(0, 0, length - 1)

  def build(self, p, l, r):
    """
    :param p: 当前运行到下标p
    :param l, r: 当前正在计算[l, r]的RMQ值
    """
    print('l, r:', l, r)

    if l == r:
      self.rmqTree[p] = self.arr[l]
    else:
      leftNodeIndex = getLeftNodeIndex(p)
      rightNodeIndex = getRightNodeIndex(p)

      self.build(leftNodeIndex, l, (l + r) // 2)
      self.build(rightNodeIndex, (l + r) // 2 + 1, r)

      self.rmqTree[p] = min(self.rmqTree[leftNodeIndex], self.rmqTree[rightNodeIndex])

  def _query(self, p, L, R, i, j):
    """
    :param i, j: 查询[i,j]的RMQ值
    :param L, R: p表示的是[L,R]的RMQ值
    """
    print('p, L, R, i, j:', p, L, R, i, j)
    if j < L or R < i:  # 不在递归调用前去掉非法值，而是进入后再判断
      return -1
    if L <= i and j <= R:
      return self.rmqTree[p]  # 这时[L,R]里的RMQ 就是[i,j]里的RMQ

    leftNodeIndex, rightNodeIndex = getLeftNodeIndex(p), getRightNodeIndex(p)
    res1 = self._query(leftNodeIndex, L, (L + R) // 2, i, j)
    res2 = self._query(rightNodeIndex, (L + R) // 2 + 1, R, i, j)

    if res1 == -1: return res2
    if res2 == -1: return res1

    return min(res1, res2)

  def query(self, i, j):
    return self._query(0, 0, len(self.arr) - 1, i, j)

  def update(self, i, n):
    """
    更新arr[i] = n
    """


if __name__ == '__main__':
  arr = [18, 17, 13, 19, 15, 11, 20]
  st = RMQSegmentTree(arr)
  print('st.rmqTree:', st.rmqTree)
  # print('st.query(0, 6):', st.query(0, 6))
  print('st.query(0, 2):', st.query(0, 2))
  # print('st.query(2, 6):', st.query(2, 6))
