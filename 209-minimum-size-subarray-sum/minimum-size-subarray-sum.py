class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        queue = deque()
        
        total = 0
        count = float('inf')
        for i in nums:
            total += i
            queue.append(i)

            while(total >= target):
                count = min(count, len(queue))
                total -= queue.popleft()
        
        if count == float('inf'):
            return 0
        return count