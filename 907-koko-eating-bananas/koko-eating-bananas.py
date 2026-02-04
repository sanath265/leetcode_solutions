class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasible(bananas):
            hour = 0
            for i in piles:
                hour += math.ceil(i/bananas)
                if hour > h:
                    return False
            return True
        
        l = 1
        r = max(piles)

        while(l < r):
            mid = (l+r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
            # print(l,r)
        # print(feasible(23))
        return l
