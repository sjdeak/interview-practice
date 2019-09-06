# https://leetcode.com/problems/interval-list-intersections/
import os
import sys

sys.setrecursionlimit(1000000)



class Solution:
  def intervalIntersection(self, A, B):  # -> List[List[int]]
    if not A or not B:
      return []

    pa, pb = 0, 0
    ans = []

    # 双指针正确性证明: 只有保证IA1已经和所有可能的B数组内的区间比对过后，IA2才会加入pool
    # pa == len(A) or pb == len(B) 时循环直接中止，因为这时不可能产生任何相交区间
    # 根据分类讨论 细致地判断不同情况下的指针移动
    while pa < len(A) and pb < len(B):
      l1, r1 = A[pa]
      l2, r2 = B[pb]

      if l1 <= l2:
        pass
      else:
        pass

      # print('pa, pb:', pa, pb)


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
