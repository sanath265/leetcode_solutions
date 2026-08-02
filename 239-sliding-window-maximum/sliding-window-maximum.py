class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        s = 0
        q = deque([])
        ans = []
        for i in range(len(nums)):
            while(q and (q[0] <= i - k)):
                q.popleft()
            
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                # print(q)
                ans.append(nums[q[0]])
        
        return ans


    
        return m