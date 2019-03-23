import os


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
  def isSymmetric(self, root) -> bool:
    # todo uf
    if not root:
      return True
    resL = self.isSymmetric(root.left)
    resR = self.isSymmetric(root.right)
    return resL


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().isSymmetric(*args), end='\n-----\n')
