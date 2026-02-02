class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        count = 0
        i = 0
        while(i<len(points)):
            a = points[i]
            if i+1 == len(points):
                return count + 1
            b = points[i+1]
            newInterval = [max(a[0], b[0]), min(a[1], b[1])]

            if newInterval[1] < newInterval[0]:
                i+=1
                count += 1
                continue
            points[i+1] = newInterval
            i+=1

            