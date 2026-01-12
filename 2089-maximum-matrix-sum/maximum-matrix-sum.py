class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        row = len(matrix)
        col = len(matrix[0])

        total = 0
        mini = float("inf")
        colNeg = 0
        for i in range(row):
            neg = 0
            for j in range(col):
                total += abs(matrix[i][j])
                mini = min(mini, abs(matrix[i][j])) 
                if matrix[i][j] < 0:
                    neg += 1
            if neg%2 ==1:
                colNeg += 1
        
        if colNeg % 2 == 1:
            return total - 2 * mini
        else:
            return total








        # colNeg = 0
        # col = len(matrix[0])
        # row = len(matrix)
        # c = 0
        # mini = 100001
        # for i in range(len(matrix)):
        #     negCount = 0
        #     for j in range(len(matrix[0])):
        #         c += abs(matrix[i][j])
        #         mini = min(mini, abs(matrix[i][j]))
        #         if matrix[i][j] < 0:
        #             negCount += 1
                
        #     if col %2 == 1:
        #         if negCount %2 == 1:
        #             colNeg += 1
        #     else:
        #         if negCount %2 == 0:
        #             colNeg += 1
        
        # # print(col, colNeg, c)

        # if col %2 == 1:
        #     if colNeg %2 == 1:
        #         colNeg = 1
        #     else:
        #         colNeg = 0
        # else:
        #     if colNeg %2 == 1:
        #         colNeg = 1
        #     else:
        #         colNeg = 0
        # if colNeg == 0:
        #     return c
        # else:
        #     return c - 2*mini
        