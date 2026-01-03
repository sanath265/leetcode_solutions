class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        same = 6
        diff = 6

        for i in range(1, n):
            nsame = diff * 2 + same * 3
            ndiff = diff * 2 + same * 2

            same = nsame
            diff = ndiff

        return (same + diff) % ((10**9) + 7)
        