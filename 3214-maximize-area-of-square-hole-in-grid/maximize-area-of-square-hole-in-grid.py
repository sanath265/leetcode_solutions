class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        hBars.sort()
        vBars.sort()
        hConti = 0
        c = 1
        for i in range(len(hBars) - 1):
            if  hBars[i] - hBars[i+1] == -1:
                c += 1
            else:
                hConti = max(c, hConti)
                c = 1
        hConti = max(c, hConti)
        vConti = 0
        c = 1
        for i in range(len(vBars) - 1):
            if  vBars[i] - vBars[i+1] == -1:
                c += 1
            else:
                vConti = max(c, vConti)
                c = 1
        vConti = max(c, vConti)
        return ((min(hConti, vConti) + 1) ** 2)