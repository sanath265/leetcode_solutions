class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row = len(heights)
        col = len(heights[0])

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        pacific = set()
        atlantic = set()

        def dfs(i, j, setocean):
            
            if (i, j) in setocean:
                return
            setocean.add((i, j))
            
            for m, n in directions:
                if 0 <= i+m < row and 0 <= j+n < col and heights[i+m][j+n] >= heights[i][j]:
                    dfs(i+m, j+n, setocean)
        
        for i in range(row):
            dfs(i, 0, pacific)
            dfs(i, col-1, atlantic)
            
        for j in range(col):
            dfs(0, j, pacific)
            dfs(row-1, j, atlantic)
        
        # print(pacific, atlantic)

        ans = []
        for i , j in pacific:
            if (i, j) in atlantic:
                ans.append([i, j])
        return ans



            
            
        