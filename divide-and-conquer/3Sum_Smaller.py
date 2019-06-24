import unittest


# 假设A中无重复项
def twoSumSmaller(A, tar, st=0):
  """
  从A中找两元组，使得和 < tar
  并不能返回所有符合条件的下标对，只保证返回的下标对对应的值对是没有遗漏的
  :param A:
  :param tar: int
  :param st: 从A[st:]里找
  :return: 符合条件的下标对个数
  """
  left, right = st, len(A) - 1
  cnt = 0
  while left < right:
    # 左右指针不断逼近，直至找到一组解 #
    while A[left] + A[right] >= tar and left < right:
      right -= 1

    if A[left] + A[right] < tar and left < right:
      cnt += right - (left + 1) + 1
      left += 1

  return cnt


def threeSumSmaller(A, tar):
  A.sort()
  ans = 0
  for i, n in enumerate(A):  # 枚举3Sum结果中下标最小的一项  twoSumOld用ignore不如用st，同样满足题意，而且更方便
    ans += twoSumSmaller(A, tar - n, i + 1)  # O(n)

  return ans


class Test(unittest.TestCase):

  def testThreeSumSmaller(self):
    self.assertEqual(threeSumSmaller([19, 28, 23, 1, 30, 15, 7, 15, 21, 5], 35), 17)

  if __name__ == "__main__":
    unittest.main()
