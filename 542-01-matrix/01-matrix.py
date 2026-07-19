class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        row = len(mat)
        col = len(mat[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


        ans = [[float('inf') for _ in range(col)] for _ in range(row)]
        q = deque([])

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for m,n in directions:
                ni = i+m
                nj = j + n
    
                if 0<=ni<row and 0<=nj<col and ans[ni][nj] == float('inf'):
                        ans[ni][nj] = ans[i][j] + 1
                        q.append((ni, nj))
        
        return ans

