# Read only region start
class UserMainCode(object):
  @classmethod
  def findPosition(cls, input1, input2, input3):
    '''
    input1 : int
    input2 : int
    input3 : int[-]

    Expected return type : int
    '''
    # Read only region end
    # Write code here
    N = input1
    Queries = input3
    # 还可以用哈希表加速
    seq = [i for i in range(1, N + 1)]
    hasE3 = False
    ans = 0
    for q in Queries:
      E, X = q
      if E == 1:
        seq.pop(0)
      elif E == 2:
        seq.remove(X)
      elif E == 3:
        ind = seq.index(X)
        print(f'E3 {X}: ind')
        ans += ind + 1
    return ans
