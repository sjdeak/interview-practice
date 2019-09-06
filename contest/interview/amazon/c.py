def MaxLIS_Lengths(numToys, tagList):
  # WRITE YOUR COE HERE

  lis, lds = {}, {}

  for i in xrange(numToys):
    if i == 0:
      lis[i] = 1
    else:
      lis[i] = lis[i - 1] + 1 if tagList[i - 1] <= tagList[i] else 1

  # 以i为开头的递减序列长度
  for i in xrange(numToys - 1, -1, -1):
    if i == numToys - 1:
      lds[i] = 1
    else:
      lds[i] = lds[i + 1] + 1 if tagList[i] >= tagList[i + 1] else 1

  # [3,7,9,13,10,7,5]
  # print 'lis', lis, '\n'
  # print 'lds', lds, '\n'

  ans = 0
  # 枚举增减串的中点
  for mid in xrange(numToys):
    choices = [2 * min(lis[mid], lds[mid]) - 1]

    ans = max([ans] + choices)

  return ans
