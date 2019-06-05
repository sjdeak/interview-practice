A, B = map(int, input().split())

if abs(A - B) > 1:
  print(2 * max(A, B) - 1)
else:
  print(A + B)
