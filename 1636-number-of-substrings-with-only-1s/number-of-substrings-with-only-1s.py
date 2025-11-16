class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        d = 0

        for i in s:
            if i == "1":
                c +=1 
            else:
                d += (c * (c+1) // 2)
                c = 0
        if c != 0:
            d += (c * (c+1) // 2)
        return d % (10**9 + 7)

        