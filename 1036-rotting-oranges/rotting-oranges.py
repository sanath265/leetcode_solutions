class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(q):
            ans = 0
            while(q):
                i, j, count = q.popleft()

                if i >= 0 and j >= 0 and i < row and j < col and grid[i][j] != 0 and grid[i][j] != 2:
                    grid[i][j] = 2
                    ans = count

                    for x, y in directions:
                        q.append((i+x, j+y, count +1))
            return ans
        
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    grid[i][j] = 1
                    q.append((i, j, 0))
        ans = bfs(q)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return ans

        
        

        