import os
from queue import Queue


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


# a → b 传递一个coin
def move(a, b, step):
  a.val -= 1
  b.val += 1
  dfs(nodes, step + 1)
  a.val += 1
  b.val -= 1


# leetcode 需要自己清理数据
def refreshGlobals():
  global nodes, ignoredups, ans
  nodes = []
  ignoredups = {}
  ans = 10 ** 20


def dfs(nodes, step):
  global ans
  coins = []
  bfsTraversal(nodes[0], lambda n: coins.append(n.val))

  # print('step:', step, '; coins:', coins)

  # keypoint: 需要细致的判重  如果步数多的走法到达过某一点，不是说就不允许步数小的走法再经过那一点了
  tcoins = tuple(coins)
  if tcoins in ignoredups and ignoredups[tcoins] <= step:
    return
  else:
    ignoredups[tcoins] = step

  if step > ans: # 最优性剪枝
    return

  if all([c == 1 for c in coins]):
    ans = min(step, ans)
    return

  # print('len(nodes)', len(nodes))
  # keypoint: 合法移动的判定需要静心设计
  for nd in nodes:
    # print('nd', nd, 'nd.val', nd.val, 'nd.left', nd.left, 'nd.right', nd.right)
    if nd.val:
      if nd.left:
        move(nd, nd.left, step)  # nd → nd.left
      if nd.right:
        move(nd, nd.right, step)  # nd → nd.right
    if nd.left and nd.left.val:
      move(nd.left, nd, step)  # nd.left → nd
    if nd.right and nd.right.val:
      move(nd.right, nd, step)  # nd.right → nd


refreshGlobals()

class Solution:
  def distributeCoins(self, root) -> int:
    bfsTraversal(root, lambda nd: nodes.append(nd)) # nodes: [TreeNode1, TreeNode2, ...]
    dfs(nodes, 0)
    ret = ans
    refreshGlobals()

    return ret


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode

  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().distributeCoins(*args), end='\n-----\n')

  # test(array2TreeNode([3,0,0]))
  # test(array2TreeNode('[0, 3, 0]'))
  # test(array2TreeNode([1,0,2]))
  # test(array2TreeNode('[1,0,0,null,3]'))
  test(array2TreeNode('[0,6,0,null,0,null,0,null,null,0]'))
