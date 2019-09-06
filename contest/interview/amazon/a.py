def powerQuest(numOfLocations, calorificVal):
  # WRITE YOUR CODE HERE
  gNums = []
  for i in xrange(0, 5):
    gNums.append(2 ** (1 << i))  # [2^1, 2^2, 2^4, 2^8, 2^16]
  length = 4

  gNums.append(sum(gNums))
  for i in xrange(length - 1):
    for j in xrange(i + 1, length):
      gNums.append(gNums[i] + gNums[j])
  for i in xrange(length - 2):
    for j in xrange(i + 1, length - 1):
      for k in xrange(j + 1, length):
        gNums.append(gNums[i] + gNums[j] + gNums[k])
  print
  gNums
  gNums = set(gNums)

  ans = 0
  for v in calorificVal:
    if v in gNums:
      ans += v

  return ans
