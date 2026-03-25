class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        row = len(rooms)
        col = len(rooms[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(q):
            while(q):
                i, j, count = q.popleft()
                if i >= 0 and j >= 0 and i < row and j < col and rooms[i][j] != -1 and rooms[i][j] >= count:
                    rooms[i][j] = count
                    for x, y in directions:
                        q.append((i+x, j+y, count + 1))
        
        q = deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        bfs(q)
        return rooms

        
        