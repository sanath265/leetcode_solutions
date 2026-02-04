class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def feasible(weight):

            day = 1
            total = 0

            for w in weights:
                total += w

                if total > weight:
                    total = w
                    day += 1
                
                if day > days:
                    return False
            return True

        l = max(weights)
        r = sum(weights)

        while(l < r):
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid+1
            # print(l, r)
        return l