class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def feasible(val):
            total = 0
            div = 1
            for i in nums:
                total += i
                if total > val:
                    total = i
                    div += 1
                    if div > k:
                        return False
            return True
        
        l = max(nums)
        r = sum(nums)
        while(l < r):
            mid = (l+r) // 2
            val = feasible(mid)
            if val:
                r = mid
            else:
                l = mid+1
        return l