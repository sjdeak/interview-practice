import unittest


def dec2KBase(n, k):
  if n == 0: return '0'
  res = ''
  while n:
    # 取出多余部分作为转换结果
    res = str(n % k) + res
    n -= n % k
    # 整除一次
    n //= k
  return res


class Test(unittest.TestCase):
  def testDec2Bin(self):
    self.assertEqual(dec2KBase(42, 2), bin(42)[2:])

  def testDec2Oct(self):
    self.assertEqual(dec2KBase(42, 8), oct(42)[2:])

  def testBorderCase(self):
    self.assertEqual(dec2KBase(0, 8), oct(0)[2:])


if __name__ == "__main__":
  # import sys;sys.argv = ['', 'Test.testInit']
  unittest.main()
