import os, sys, shutil, glob, re
import time, calendar
from datetime import datetime, timezone
import hashlib, zipfile, zlib
from math import *
from operator import itemgetter
from functools import wraps, cmp_to_key
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int how many tuples there are e
        """
        res = 0
        # cl = [Counter(l) for l in [A, B, C, D]]
        
        c1 = Counter([a+b for a in A for b in B])
        c2 = Counter([c+d for c in C for d in D])
        
        for ps in c1:
            if -ps in c2:
                res += c1[ps]*c2[-ps]
        # for a in cl[0]:
        #     for b in cl[1]:
        #         for c in cl[2]:
        #             if -(a+b+c) in cl[3]:
        #                 res += cl[0][a] * cl[1][b] * cl[2][c] * cl[3][-(a+b+c)]
        return res
        

if __name__ == '__main__' and ('SJDEAK' in os.environ):
    def test(*args):
        print('测试: ', *args,
              '\n结果: ', Solution().fourSumCount(*args), end='\n-----\n')

    test([1,2],[-2,-1],[-1,2],[0,2])
    test([-1,-1],[-1,1],[-1,1],[1,-1])