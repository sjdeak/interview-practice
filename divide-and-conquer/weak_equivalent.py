import unittest


def weakEquivalent(a, b):
  lenA = len(a)
  if lenA == 1:
    return a == b

  mid = lenA // 2
  a1, a2 = a[:mid], a[mid:]
  b1, b2 = b[:mid], b[mid:]

  return (weakEquivalent(a1, b1) and weakEquivalent(a2, b2)) or (weakEquivalent(a1, b2) and weakEquivalent(a2, b1))


class Test(unittest.TestCase):

  def test(self):
    self.assertEqual(weakEquivalent('abbaabba', 'baababab'), True)
    self.assertEqual(weakEquivalent('a', 'a'), True)
    self.assertEqual(weakEquivalent('a', 'b'), False)


if __name__ == "__main__":
  unittest.main()
