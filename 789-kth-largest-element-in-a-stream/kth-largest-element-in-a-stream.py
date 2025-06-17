class KthLargest:
    k = 0
    # nums = []
    heap = []
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k or self.heap[0] < val:
            heapq.heappush(self.heap, val)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        return self.heap[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)