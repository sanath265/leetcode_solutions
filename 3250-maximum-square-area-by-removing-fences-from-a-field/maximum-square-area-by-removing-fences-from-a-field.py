class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """

        if n == m:
            return ((n-1)*(n-1))  % (10**9 + 7)
        hFences.sort()
        vFences.sort()
        v = set()
        
        a = []
        
        hFences.append(m)
        vFences.append(n)
        for i in range(len(vFences)):
            if i == 0:
                a.append(vFences[i] - 1)
            else:
                a.append(vFences[i] - vFences[i-1])
        vFence = a

        a = []
        for i in range(len(hFences)):
            if i == 0:
                a.append(hFences[i] - 1)
            else:
                a.append(hFences[i] - hFences[i-1])
        hFence = a

        for i in range(len(vFence)):
            c = 0
            for j in range(i, len(vFence)):
                c += vFence[j]
                v.add(c)
        # print(v, vFence)
        ans = 0
        for i in range(len(hFence)):
            c = 0
            for j in range(i, len(hFence)):
                c += hFence[j]
                if c in v:
                    ans = max(ans, c)
        if ans == 0:
            return -1
        return (ans**2) % (10**9 + 7)

        