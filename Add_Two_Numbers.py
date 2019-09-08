# https://leetcode.com/problems/add-two-numbers/
import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy

sys.setrecursionlimit(1000000)


class Solution:
  def addTwoNumbers(self, l1, l2):  # -> ListNode
    # l1, l2: two non-empty linked lists
    s = l1.val + l2.val
    up = s >= 10
    val = s % 10
    st = ListNode(val)
    now = st
    l1, l2 = l1.next, l2.next
    while l1 or l2:
      v1 = l1.val if l1 else 0
      v2 = l2.val if l2 else 0

      print('v1, v2, up:', v1, v2, up)

      s = v1 + v2 + int(up)
      up = s >= 10
      val = s % 10
      now.next = ListNode(val)
      now = now.next

      if l1: l1 = l1.next
      if l2: l2 = l2.next

    if up:
      now.next = ListNode(1)

    return st


if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from utils.linkedlist import ListNode, integerListToListNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().addTwoNumbers(*args), end='\n-----\n')


  test(integerListToListNode([2, 4, 3]), integerListToListNode([5, 6, 4]))
  # test()
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
