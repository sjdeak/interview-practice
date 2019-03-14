class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def nextStep(n):
            return sum([int(_)**2 for _ in list(str(n))])
            
        s = set()
        while n != 1:  # 循环终止条件
            s.add(n)
            
            # print(n)
            
            n = nextStep(n)
            if n in s:
                return False
            
        return True
    
    
if __name__ == '__main__':
    def test(n):
        print(n, Solution().isHappy(n))
    
    test(19)
    test(1)
    test(22)