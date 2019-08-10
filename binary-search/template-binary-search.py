def binarySearch(A, x):
  """A单调递增, 找是否有x, 如果有则返回下标"""
  left, right = 0, len(A) - 1
  while left <= right:
    mid = left + (right - left) // 2

    if A[mid] > x:
      right = mid - 1
    elif A[mid] < x:
      left = mid + 1
    else:
      return mid

  return -1


def geLeftmost(A, x):  # lower_bound
  """A单调递增, 找>=x的最左侧元素"""
  pass


def leRightmost(A, x):  # upper_bound
  """A单调递增, 找<=x的最右侧元素"""
  left, right = 0, len(A) - 1
  while left < right:
    # print('A, x, left, right:', A, x, left, right)
    # 用偏右侧的mid以保证循环会结束
    mid = right - (right - left) // 2
    if A[mid] < x:
      left = mid
    else:
      right = mid - 1

  # 最终检查
  if A[left] <= x:
    return left
  else:
    return -1
