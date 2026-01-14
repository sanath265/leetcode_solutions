class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """

        # def check():

        
        ySquares = []
        totalArea = 0
        for i in squares:
            ySquares.append([i[1], i[1] + i[2], i[2]])
            totalArea += (i[2] ** 2)

        ySquares.sort(key = lambda x: x[1])

        print(totalArea)
        above = 0
        below = float(totalArea)

        b = 0
        a = ySquares[-1][1]
        while(abs(b-a) > 10**(-5)): 
            mid = (b + a) / 2.0
            i = 0
            below = 0.0
            while(i < len(squares)):
                val = ySquares[i]
                if val[1] <= mid:
                    below += val[2] ** 2
                elif val[0] <= mid < val[1]:
                    below += val[2] * (mid - val[0])
                
                i+=1
            
            above = totalArea - below
                
            if below >= totalArea/2.0:
                a = mid
            else:
                b = mid
            print(mid, b, a, below, above)

        return (b+a)/2.0
