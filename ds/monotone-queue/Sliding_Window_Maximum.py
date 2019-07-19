# https://leetcode.com/problems/sliding-window-maximum/
import os
import sys
from collections import deque

sys.setrecursionlimit(1000000)


# template
def slidingWindow(A, k):
  q = deque()

  for n in A:
    if len(q) < k:
      q.append(n)
    else:
      q.popleft()
      q.append(n)

    if len(q) == k:
      pass

def minSlidingWindow(nums, k):  # -> List[int]
  # mq里存放下标 指向可能会是窗口最值的值  单增
  mq = deque()
  ans = []

  for i in range(len(nums)):
    if mq and mq[0] < i - k + 1:
      mq.popleft()

    while mq and nums[mq[-1]] >= nums[i]:
      mq.pop()
    mq.append(i)
    print('mq:', mq)

    if i >= k - 1:
      ans.append(nums[mq[0]])
      print('ans:', ans)

  return ans


class Solution:
  def maxSlidingWindow(self, nums, k):  # -> List[int]
    # mq里存放下标 指向可能会是窗口最值的值  单调递减
    mq = deque()
    ans = []

    for i in range(len(nums)):
      if mq and mq[0] < i - k + 1:
        mq.popleft()

      while mq and nums[mq[-1]] <= nums[i]:  # 排除mq里所有在i前面但值比A[i]小的元素 使得队列单调递减
        mq.pop()
      mq.append(i)
      print('mq:', mq)

      if i >= k - 1:  # 当i已经加入窗口后的窗口最值
        ans.append(nums[mq[0]])
        print('ans:', ans)

    return ans


if __name__ == '__main__' and ('SJDEAK' in os.environ):

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().maxSlidingWindow(*args), end='\n-----\n')


  test([1, 3, -1, -3, 5, 3, 6, 7], 3)
  # test()
else:
  print = lambda *args, **kwargs: None
