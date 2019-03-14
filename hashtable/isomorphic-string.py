# class Solution:
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         d = {}  # t->s 映射表
#         for i, ch in enumerate(s):
#             if t[i] not in d:
#                 d[t[i]] = ch
#             elif d[t[i]] != ch:
#                 return False
#
#         return True

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        inverseD = {}
        for i, ch in enumerate(s):
            if ch not in d:  # 没有映射规则
                if t[i] not in inverseD:
                    d[ch] = t[i]  # 新建
                    inverseD[t[i]] = ch
                else:
                    return False
            elif d[ch] != t[i]:
                return False
        
        return True

if __name__ == '__main__':
    def test(s, t):
        print(s, t, Solution().isIsomorphic(s, t))
    
    
    test('egg', 'add')
    test('foo', 'bar')
    test('paper', 'title')
    test('ab', 'aa')
    
