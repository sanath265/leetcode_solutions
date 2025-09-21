class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = [0 for i in prices]
        pre[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            pre[i] = max(pre[i+1], prices[i])
        m = 0
        for i in range(len(prices) - 1):
            m = max(m, pre[i+1] - prices[i])
        
        return m
