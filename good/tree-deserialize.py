from queue import Queue


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


def preorderTraversal(node, func):
  if not node:
    return
  func(node)
  preorderTraversal(node.left, func)
  preorderTraversal(node.right, func)


def inorderTraversal(node, func):
  if not node:
    return
  inorderTraversal(node.left, func)
  func(node)
  inorderTraversal(node.right, func)


def postorderTraversal(node, func):
  if not node:
    return
  postorderTraversal(node.left, func)
  postorderTraversal(node.right, func)
  func(node)


def bfsTraversal(root, func):
  q = Queue()
  q.put(root)

  while not q.empty():
    now = q.get()
    if not now:
      continue
    func(now)
    q.put(now.left)
    q.put(now.right)


def array2TreeNode(string):
  """
  把层序遍历再模拟一遍 凭借arr填充树的数据和维持遍历
  :param string: 层序遍历结果字符串
  :return: TreeNode root
  """
  arr = [None if val == 'null' else int(val) for val in string.strip("[]{}").split(',')]

  if not len(arr):
    return None

  root = TreeNode(arr[0])
  q = Queue()
  q.put((0, root))

  ind = 0

  while not q.empty():
    i, now = q.get()
    print('(i, now)', (i, now))
    if not now:
      continue

    leftI = ind + 1
    if leftI < len(arr) and arr[leftI] is not None:
      now.left = TreeNode(arr[leftI])
      q.put((leftI, now.left))
    rightI = ind + 2
    if rightI < len(arr) and arr[rightI] is not None:
      now.right = TreeNode(arr[rightI])
      q.put((rightI, now.right))
    ind += 2

  return root


if __name__ == '__main__':
  def test(arr):
    root = array2TreeNode(arr)
    bfsTraversal(root, lambda nd: print(nd.val))


  # test([1, None, 2, 3])
  # test([5,4,7,3,None,2,None,-1,None,9])
  test([1, None, 2, 3])
