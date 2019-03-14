from collections import Counter


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        for n in nums:
            if c[n] == 1:
                return n