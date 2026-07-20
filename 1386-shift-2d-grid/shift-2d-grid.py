class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        row = len(grid)
        col = len(grid[0])

        k = k % (row * col)

        def findpos(i, j):

            nj = (j+k) % (col)

            ni = (i + (j+k)//col) % row

            return (ni, nj)
        
        ans = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                ni, nj = findpos(i, j)
                # print(nj, ni)
                ans[ni][nj] = grid[i][j]
        return ans
        