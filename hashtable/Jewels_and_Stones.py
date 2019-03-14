

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = set(J)
        return len(list(filter(lambda item: item in s, S)))
        


if __name__ == '__main__':
    def test(*args, **kwargs):
        print(*args, Solution().numJewelsInStones(*args, **kwargs), **kwargs)

    test("aA", "aAAbbbb")