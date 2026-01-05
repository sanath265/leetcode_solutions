class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        colNeg = 0
        col = len(matrix[0])
        row = len(matrix)
        c = 0
        mini = 100001
        for i in range(len(matrix)):
            negCount = 0
            for j in range(len(matrix[0])):
                c += abs(matrix[i][j])
                mini = min(mini, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    negCount += 1
                
            if col %2 == 1:
                if negCount %2 == 1:
                    colNeg += 1
            else:
                if negCount %2 == 0:
                    colNeg += 1
        
        # print(col, colNeg, c)

        if col %2 == 1:
            if colNeg %2 == 1:
                colNeg = 1
            else:
                colNeg = 0
        else:
            if colNeg %2 == 1:
                colNeg = 1
            else:
                colNeg = 0
        if colNeg == 0:
            return c
        else:
            return c - 2*mini
        