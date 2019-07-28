# https://leetcode.com/problems/interval-list-intersections/
import os
import sys

sys.setrecursionlimit(1000000)


class Solution:
  def intervalIntersection(self, A, B):  # -> List[List[int]]
    if not A or not B:
      return []

    pa, pb = 0, 0
    pool = [None, None]  # 待选池
    ans = []

    # 双指针正确性证明: 当pa加入pool时 先前一个pa已经和所有有可能相交的B内的区间比对过了
    while pa < len(A) or pb < len(B):
      if pa == len(A):
        pool[1] = B[pb]
        pb += 1
      elif pb == len(B):
        pool[0] = A[pa]
        pa += 1
      elif A[pa][0] <= B[pb][0]:
        pool[0] = A[pa]
        pa += 1
      elif A[pa][0] > B[pb][0]:
        pool[1] = B[pb]
        pb += 1

      print('pa, pb:', pa, pb)

      if all(map(bool, pool)):
        l1, r1 = pool[0]
        l2, r2 = pool[1]

        if r2 >= l1 and l2 <= r1:  # 先保证两个区间有相交部分
          ans.append([max(l1, l2), min(r1, r2)])  # 然后求相交部分

        print('pool after:', pool)

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
