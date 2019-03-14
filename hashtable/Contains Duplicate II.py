# time complexity: O(n)

from collections import defaultdict


class Solution:
    def _check(self, indexList, k):
        if len(indexList) <= 1:
            return False
        return min([indexList[_+1]-indexList[_] for _ in range(len(indexList)-1)]) <= k
         
    
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dd = defaultdict(list)
        
        for i, n in enumerate(nums):
            dd[n].append(i)
            
        for n in dd:
            if self._check(dd[n], k):
                return True
        else:
            return False


if __name__ == '__main__':
    def test(nums, k):
        print(nums, k, Solution().containsNearbyDuplicate(nums, k))
    
    
    test([1,2,3,1,2,3], 2)
    test([1,0,1,1], 1)
    test([1,2,3,1], 3)
    