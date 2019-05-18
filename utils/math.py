def A(m, n):
  return 1 if n == 0 else A(m, n - 1) * (m - n + 1)


def C(m, n):  # todo wrong
  return A(m, n) // A(n, n)


if __name__ == '__main__':
  print('C(4,2):', C(4, 2))
