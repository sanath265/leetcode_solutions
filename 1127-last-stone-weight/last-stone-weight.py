class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesN = [-i for i in stones]
        heapq.heapify(stonesN)
        while(len(stonesN) > 1):
            # print(stonesN)
            s1 = -heapq.heappop(stonesN)
            s2 = -heapq.heappop(stonesN)

            if s1 != s2:
                heapq.heappush(stonesN, -abs(s1-s2))
            
        return -stonesN[0] if len(stonesN) > 0 else 0