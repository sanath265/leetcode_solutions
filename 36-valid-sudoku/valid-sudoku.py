class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c = False
        row= 9
        col = 9
        for i in range(row):
            a = {}
            b = {}
            c = {}
            for j in range(col):
                if board[i][j] != ".":
                    if board[i][j] not in a:
                        a[board[i][j]] = 1
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in b:
                        b[board[j][i]] = 1
                    else:
                        return False
                
                if board[(i//3) * 3 + j//3][(i%3) * 3 + j % 3] != ".":
                    if board[(i//3) * 3 + j//3][(i%3) * 3 + j % 3]  not in c:
                        c[board[(i//3) * 3 + j//3][(i%3) * 3 + j % 3] ] = 1
                    else:
                        return False
        return True
