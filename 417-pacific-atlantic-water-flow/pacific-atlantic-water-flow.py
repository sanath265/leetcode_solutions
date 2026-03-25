class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        col = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ans = []
        dp = [[-1 for _ in range(col)] for _ in range(row)]

        def dfs(i, j, visited):

            if (i, j) in visited:
                return
            
            visited.add((i, j))
            for x, y in directions:
                ni = i+x
                nj = j + y

                if ni >= 0 and nj >= 0 and ni < row and nj < col and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)

        pacific = set()
        atlantic = set()
        for i in range(row):
            dfs(i, 0, pacific)
            dfs(i, col-1, atlantic)
        
        for i in range(col):
            dfs(0, i, pacific)
            dfs(row - 1, i, atlantic)

        # print(pacific, atlantic)

        return list(pacific.intersection(atlantic))


    



        