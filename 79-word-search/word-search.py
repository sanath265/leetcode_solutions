class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        output = False


        def dfs(x, y, pos):
            if pos == len(word):
                return True
            
            if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0 or board[y][x] != word[pos]:
                return False
            
            temp = board[y][x]
            board[y][x] = 1
            found =  (dfs(x - 1, y, pos + 1) or 
                    dfs(x + 1, y, pos + 1) or 
                    dfs(x, y + 1, pos + 1) or 
                    dfs(x, y - 1, pos + 1))
            board[y][x] = temp

            return found
            
        for i in range(len(board[0])):
            for j in range(len(board)):
                output = output or dfs(i, j, 0)
        return output
        