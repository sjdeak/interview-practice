# 剩下第七页第八页还没看
import bisect

raw_input = input
T = int(raw_input())


def csb(n):  # 统计n里有几个1
  count = 0
  while (n):
    count += n & 1
    n >>= 1
  return count % 2


def solve():
  N, Q = [int(_) for _ in raw_input().split()]
  arr = [csb(int(_)) for _ in raw_input().split()]  # arr[i] = A[i]的1的个数
  piv = 0
  res = []
  ones = []
  piv = sum(arr)
  for i in range(N):
    if arr[i]:
      ones.append(i)

  for i in range(Q):
    pos, num = [int(_) for _ in raw_input().split()]
    num = csb(num)
    if num == arr[pos]:
      pass
    elif num:  # 修改值为xor-odd
      arr[pos] = num
      piv += 1
      bisect.insort(ones, pos)  # 把pos插入ones里，同时不打乱顺序
    else:  # 修改值为xor-even
      arr[pos] = num
      piv -= 1
      del ones[bisect.bisect_left(ones, pos)]

    if piv % 2 == 0:  # 整个数组为xor-odd区间
      res.append(N)
    else:
      res.append(max(N - ones[0] - 1, ones[-1]))  # 前面维护ones的顺序，是为了这里要出结果
  return res


for t in range(T):
  res = solve()
  print("Case #{}: {}".format(t + 1, " ".join(map(str, res))))
