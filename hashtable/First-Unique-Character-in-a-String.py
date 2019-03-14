from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i