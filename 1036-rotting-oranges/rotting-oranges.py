class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        ans = 0

        q = deque([])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        
        while(q):
            i, j, count = q.popleft()
            
            for m, n in directions:
                ni = i + m
                nj = j + n

                if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni, nj, count + 1))
                    ans = max(ans, count+1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        
        return ans
        
