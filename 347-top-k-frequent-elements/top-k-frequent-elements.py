class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        c = []

        for i in d:
            heapq.heappush(c, [d[i], i])
            if len(c) > k:
                heapq.heappop(c)
        
        return [i[1] for i in c]

        
