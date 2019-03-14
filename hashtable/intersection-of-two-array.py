# 求去重的交集
# 先求交，再把交集去重

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        res = []
        for n in nums2:
            if n in s1:
                res.append(n)
    
        return list(set(res))

