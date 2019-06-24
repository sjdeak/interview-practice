import operator
import unittest


def merge(A1, A2, cmp=operator.lt):
  i1, i2 = 0, 0
  l1, l2 = len(A1), len(A2)
  res = []
  while i1 < l1 or i2 < l2:
    if i1 == l1:
      res.append(A2[i2])
      i2 += 1
      continue
    if i2 == l2:
      res.append(A1[i1])
      i1 += 1
      continue

    n1, n2 = A1[i1], A2[i2]
    if cmp(n1, n2):
      res.append(n1)
      i1 += 1
    else:
      res.append(n2)
      i2 += 1

  return res


# 思路乱掉了，一会想就地排序 一会想返回新数组
# def mergeSort(A, l, r):
#
#   #* 特判 *#
#   if r-l+1 < 2:
#     return A
#   #* 归 *#
#   half = (r+l) // 2
#
#   print('l, r, half:', l, r, half)
#
#   sortedA1 = mergeSort(A, l, half)
#   print('sortedA1:', sortedA1)
#   for i in range(l, half+1):
#     A[i] = sortedA1[i-l]
#
#   sortedA2 = mergeSort(A, half+1, r)
#   print('sortedA2:', sortedA2)
#   for i in range(half+1, r+1):
#     A[i] = sortedA2[i-half-1]
#
#   #* 并 *#
#   return merge(A[l:half+1], A[half+1:r+1])


# 这样空间复杂度是O(nlogn) 但代码更干净
def mergeSort(A):
  # * 特判 *#
  if len(A) < 2:
    return A
  # * 归 *#
  half = len(A) // 2
  A1 = mergeSort(A[:half])
  A2 = mergeSort(A[half:])
  # * 并 #
  return merge(A1, A2)


# 开新数组
def quickSort(A):
  pass


# 就地更易
def quickSortInPlace(A):
  # 返回pivot的下标
  def divideByPivot(l, r):
    print('l,r:', l, r)
    while l < r:
      while A[r] > A[l]:  # A[l]为pivot
        r -= 1
      A[l], A[r] = A[r], A[l]
      while A[l] < A[r]:  # A[r]为pivot
        l += 1
      A[l], A[r] = A[r], A[l]

    print('res pivotI:', l)
    return l

  def qs(l, r):
    nonlocal A
    if r - l + 1 <= 1:
      return

    pivotI = divideByPivot(l, r)
    qs(l, pivotI - 1)
    qs(pivotI + 1, r)

  qs(0, len(A) - 1)


class Test(unittest.TestCase):

  def testMerge(self):
    A1 = [1, 5, 9]
    A2 = [2, 6, 9, 10]

    self.assertEqual(merge(A1, A2), [1, 2, 5, 6, 9, 9, 10])
    # self.assertEqual(merge(A1, A2), [10,2,5,6,9,9,1])

  def testMergeSort(self):
    A = [6, 10, 13, 45, 2, 6, 34, 76, 3, 25]
    self.assertEqual(mergeSort(A), [2, 3, 6, 6, 10, 13, 25, 34, 45, 76])

  def testQuickSort(self):
    # A = [6, 10, 13, 45, 2, 6, 34, 76, 3, 25]
    # quickSortInPlace(A)
    # self.assertEqual(A, [2, 3, 6, 6, 10, 13, 25, 34, 45, 76])

    A = [5, 1, 9, 8, 3, 6, 4, 7]
    quickSortInPlace(A)
    self.assertEqual([1, 3, 4, 5, 6, 7, 8, 9], A)


if __name__ == "__main__":
  # import sys;sys.argv = ['', 'Test.testInit']
  unittest.main()
