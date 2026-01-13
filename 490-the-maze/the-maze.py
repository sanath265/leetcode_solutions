class Solution(object):
    ans = False
    row = 0
    col = 0
    directions = [[1,0], [-1, 0], [0,1], [0,-1]]
    visit = [[False for _ in col] for _ in range(row)]

    def isRightPos(self, x, y, maze):
        return (x < 0 or y < 0 or x >= self.row or y >= self.col or maze[x][y] == 1 )
    
    def dfs(self, start, dest, maze, direction):
        print(start)
        if self.ans:
            return
        
        # self.visit[start[0]][start[1]] = True

        if start == dest and self.isRightPos(start[0] + direction[0], start[1] + direction[1], maze):
            self.ans = True

        if self.isRightPos(start[0] + direction[0], start[1] + direction[1], maze):
            if self.visit[start[0]][start[1]]:
                return
            self.visit[start[0]][start[1]] = True

            if start == dest:
                self.ans = True
                return
            for i in self.directions:
                self.dfs(start, dest, maze, i)
        else:
            newStart = [start[0] + direction[0], start[1] + direction[1]]
            self.dfs(newStart, dest, maze, direction)
            
    def hasPath(self, maze, start, destination):
        self.row = len(maze)
        self.col = len(maze[0])
        self.visit = [[False for _ in range(self.col)] for _ in range(self.row)]

        for d in self.directions:
            self.dfs(start, destination, maze, d)

        return self.ans

        
        