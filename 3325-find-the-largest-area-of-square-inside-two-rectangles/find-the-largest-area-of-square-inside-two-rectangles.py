class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        area = 0
        for i in range(len(bottomLeft)):
            for j in range(i+1, len(bottomLeft)):

                x = -max(bottomLeft[i][1], bottomLeft[j][1]) + min(topRight[i][1], topRight[j][1])
                y = -max(bottomLeft[i][0], bottomLeft[j][0]) + min(topRight[i][0], topRight[j][0])
                x = max(0, x)
                y = max(0, y)
                area = max(area, min(x, y)**2)
        return area
        