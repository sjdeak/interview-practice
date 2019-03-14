class Solution:
    @staticmethod
    def howLongSinceHere(s, i):
        s_set = set()
        s = s[i:]
        cnt = 0
        for ch in s:
            if ch not in s_set:
                s_set.add(ch)
                cnt += 1
            else:
                break
        return cnt
        
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max([self.howLongSinceHere(s, i) for i in range(len(s))] or [0])


if __name__ == '__main__':
    def test(*args, **kwargs):
        print(*args, Solution().lengthOfLongestSubstring(*args, **kwargs), **kwargs)
    
    
    test("abcabcbb")
    test("")