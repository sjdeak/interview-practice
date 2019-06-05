# Read only region start
class UserMainCode(object):
  @classmethod
  def hungryFish(cls, input1, input2, input3, input4):
    '''
    input1 : int
    input2 : int
    input3 : int
    input4 : int[-]

    Expected return type : int[]
    '''
    # Read only region end
    # Write code here
    N, M, Q, Queries = input1, input2, input3, input4

    # Caution: 下标从1开始
    ans = [-1] * (M + 1)
    sizeA = [0] * (M + 1)
    for query in Queries:
      E, n1, n2 = query
      if E == 1:
        ans[n2] = n1
        sizeA[n1] += 1
      else:
        if sizeA[n1] > sizeA[n2]:  # A类 大鱼吃小鱼 n1吃n2
          sizeA[n1] += sizeA[n2]
          for i in range(1, M + 1):
            if ans[i] == n2:
              ans[i] = n1
    return ans[1:]
