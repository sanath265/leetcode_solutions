class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        newMat = [[0 for _ in range(c)] for _ in range(r)]

        row = 0
        col = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if col == c:
                    col = 0
                    row += 1
                newMat[row][col] = mat[i][j]

                col += 1
        return newMat
