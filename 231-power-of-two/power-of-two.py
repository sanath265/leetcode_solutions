class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # print(15 & 16)
        if n == 0:
            return False
        if (n & n-1) == 0:
            return True
        return False