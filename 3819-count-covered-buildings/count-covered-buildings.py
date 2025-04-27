class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # buildings.sort()
        # print(buildings)

        row = [(n+1, 0) for _ in range(n+1)]
        col = [(n+1, 0) for _ in range(n+1)]

        for i in buildings:
            r = i[0]
            c = i[1]
            row[r] = (min(row[r][0], c), max(row[r][1], c))
            col[c] = (min(col[c][0], r), max(col[c][1], r))
        # print(row, col)

        z = 0
        for i in buildings:
            h = False
            v = False
            
            r = i[0]
            c = i[1]

            # print(i, row[r], col[c])
            if i[1] > row[r][0] and i[1] < row[r][1] and (row[r][1] != 0 and row[r][0] != n+1):
                h = True

            if i[0] > col[c][0]  and i[0] < col[c][1] and (col[c][1] != 0 and col[c][0] != n+1):
                v = True

            if h and v:
                z += 1
                # print("buil", i)
        return z
            
            
        