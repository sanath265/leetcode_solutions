class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x

        if x == 0 or x ==1:
            return x
        ans = 0
        while(left <= right):
            mid = (left + right) // 2

            if mid*mid <= x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        print(ans)
        return left - 1