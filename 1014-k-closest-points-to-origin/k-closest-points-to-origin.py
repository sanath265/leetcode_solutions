class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            heapq.heappush(heap, (i[0]**2 + i[1]**2, i))
        result = []
        for i in range(k):
            s = heapq.heappop(heap)
            result.append(s[1])
        
        return result