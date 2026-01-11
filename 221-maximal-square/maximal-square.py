class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        dp = [[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if (i - 1 < 0 and j - 1 < 0) or i-1 < 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) != 0:
                    dp[i][j] = int(min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])) + int(matrix[i][j])
                
                ans = max(ans, dp[i][j])
        # print(dp)
        return ans * ans

        