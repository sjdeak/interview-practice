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

def array2TreeNode(arr):
  if not len(arr):
    return None

  root = TreeNode(arr[0])
  q = Queue()
  q.put((0, root))

  while not q.empty():
    i, now = q.get()
    print('(i, now)', (i, now))
    if not now:
      continue

    leftI, rightI = 2 * i + 1, 2 * i + 2
    if leftI < len(arr) and arr[leftI] is not None:
      now.left = TreeNode(arr[leftI])
      q.put((leftI, now.left))
    if rightI < len(arr) and arr[rightI] is not None:
      now.right = TreeNode(arr[rightI])
      q.put((rightI, now.right))

  return root


if __name__ == '__main__':
  def test(arr):
    root = array2TreeNode(arr)
    bfsTraversal(root, lambda nd: print(nd.val))

  test([1, None, 2, 3])