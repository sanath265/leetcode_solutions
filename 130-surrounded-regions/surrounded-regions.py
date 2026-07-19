class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row = len(board)
        col = len(board[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j):

            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == "X" or board[i][j] == "S":
                return
            
            board[i][j] = "S"

            for m,n in directions:
                dfs(i+m, j+n)
        
        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        

        for i in range(row):
            for j in range(col):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"