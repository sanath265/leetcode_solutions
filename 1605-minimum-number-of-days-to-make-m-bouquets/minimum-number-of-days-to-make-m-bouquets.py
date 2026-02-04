class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(day):
            adjFlowers = 0
            bouquetCount = 0
            for i in bloomDay:
                if i <= day:
                    adjFlowers += 1
                else:
                    adjFlowers = 0
                if adjFlowers == k:
                    bouquetCount += 1
                    adjFlowers = 0
                if bouquetCount == m:
                    return True
            return False

        if m * k > len(bloomDay):
            return -1
        
        l = min(bloomDay)
        r = max(bloomDay)

        while(l < r):
            mid = (l+r)//2

            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
                