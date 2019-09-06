# https://leetcode.com/problems/interval-list-intersections/
import os
import sys

sys.setrecursionlimit(1000000)


class Solution:
  def intervalIntersection(self, A, B):  # -> List[List[int]]
    def checkPool():
      """
      对于两个区间 I1 = [l1, r1], I2 = [l2, r2]  (I1, I2的相对位置没有要求)

      判断是否有相交部分: `r2 >= l1 and l2 <= r1`
      若已知它们有相交部分, 则相交部分为 `[max(l1, l2), min(r1, r2)]`
      """
      if all(map(bool, pool)):
        l1, r1 = pool[0]
        l2, r2 = pool[1]

        if r2 >= l1 and l2 <= r1:  # 先保证两个区间有相交部分
          ans.append([max(l1, l2), min(r1, r2)])  # 然后求相交部分

        print('pool after:', pool)

    if not A or not B:
      return []

    pa, pb = 0, 0
    pool = [None, None]  # 比对池
    ans = []

    # 双指针算法正确性证明
    # 即证明 所有相交的区间  都会被加入比对池
    # 当A[2]加入pool时 保证A[1]已经和所有有可能相交的B内的区间比对过了
    while pa < len(A) or pb < len(B):
      if pa == len(A):
        pool[1] = B[pb]
        pb += 1
      elif pb == len(B):
        pool[0] = A[pa]
        pa += 1
      else:
        l1, r1 = A[pa]
        l2, r2 = B[pb]

        # 最核心的思路
        if l1 <= l2:  # 所有左边缘不能越过A[2].l的B内区间 都有可能和A[1]相交
          pool[0] = A[pa]
          pa += 1
        else:  # 所有左边缘不能越过B[2].l的A内区间 都有可能和B[1]相交
          pool[1] = B[pb]
          pb += 1

      # print('pa, pb:', pa, pb)
      checkPool()  # 检查区间比对池   比对池中的区间可能会相交

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().intervalIntersection(*args), end='\n-----\n')


  test([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])
  test([[5, 10]], [[5, 6]])
  test([[8, 15]], [[2, 6], [8, 10], [12, 20]])
else:
  print = lambda *args, **kwargs: None
