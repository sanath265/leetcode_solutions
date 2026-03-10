class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = {}
        def dfs(i, coveredDay):
            cost = 0

            if i == len(days):
                return 0
            
            if (i, coveredDay) in dp:
                return dp[(i, coveredDay)]

            if days[i] <= coveredDay:
                # print(i, coveredDay)
                cost =  dfs(i+1,coveredDay)
            else:
                cost = min(costs[0] + dfs(i+1,days[i]), costs[1] + dfs(i+1, days[i] + 6), costs[2] + dfs(i+1, days[i] + 29))
            dp[(i, coveredDay)] = cost
            return cost
        return dfs(0, 0)
            
            

        