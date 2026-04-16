class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        row  = len(grid)
        col = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1

        ans = float("inf")

        q = deque()
        q.append([0, 0, 1])
        visited = set()
        while q:
            i, j, count = q.popleft()

            if (i, j) in visited:
                continue

            if i == row-1 and j == col-1:
                return count
                
            visited.add((i, j))
            if i >= 0 and j >=0 and i < row and j < col and grid[i][j]==0:
                for x, y in directions:
                    q.append([i+x, j+y, count + 1])
        
        return -1