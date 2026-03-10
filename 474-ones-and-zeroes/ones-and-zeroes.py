class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        strsLen = []

        for i in strs:
            zeros = 0
            ones = 0
            for j in i:
                if j == "1":
                    ones += 1
                else:
                    zeros += 1
            strsLen.append((zeros, ones))
        print(strsLen)
        
        dp = {}
        def dfs(i, total):
            res = 0
            if i == len(strs):
                return 0

            if (i, total) in dp:
                return dp[(i, total)]

            zeros = total[0] + strsLen[i][0]
            ones = total[1] + strsLen[i][1]

            if zeros > m or ones > n:
                res = dfs(i+1, total)
            else:
                res = max(1 + dfs(i+1, (zeros, ones)), dfs(i+1, total))
            
            # print(res, i, total)
            dp[(i, total)] = res
            return res
        
        return dfs(0, (0, 0))
            
        