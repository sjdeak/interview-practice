from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1, c2 = Counter(nums1), Counter(nums2)
        
        ans = []
        for k in c1:
            if k in c2:
                ans += [k] * min(c1[k], c2[k])
                
        return ans