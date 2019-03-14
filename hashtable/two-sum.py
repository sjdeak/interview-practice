# 两个不同的数 / 两个相同的数  n1 + n2 = target
# 题面说了不允许相同的数用两次
# 又说只有唯一解
# 有重的数必然不会是n1, n2


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if nums.count(target/2) == 2:
            l = nums.index(target/2)
            r = l+1 + nums[l+1:].index(target/2)
            return [nums.index(target/2), r]
            
        
        d = {n: i for i, n in enumerate(nums)}
        for n in d:
            if target - n in d:
                return [d[n], d[target - n]]
            
