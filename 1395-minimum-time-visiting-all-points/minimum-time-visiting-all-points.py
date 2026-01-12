import math
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        time = 0
        for i in range(1, len(points)):
            start = points[i-1]
            end = points[i]
            xAbs = abs(end[0] - start[0])
            yAbs = abs(end[1] - start[1])
                
            # if abs(xAbs //yAbs) == 1:
            #     time += xAbs
            
            # else:
            val = min(xAbs, yAbs)
                
            newPoint = []
            if end[0] < start[0]:
                newPoint.append(start[0] - val)
            else:
                newPoint.append(start[0] + val)
                
            if end[1] < start[1]:
                newPoint.append(start[1] - val)
            else:
                newPoint.append(start[1] + val)

            time += abs(newPoint[0] - start[0]) + abs(newPoint[0] - end[0]) + abs(newPoint[1] - end[1])
        return time
            


                    


        