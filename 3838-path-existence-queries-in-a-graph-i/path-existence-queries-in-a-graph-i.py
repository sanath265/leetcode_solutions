class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # if n == 1:
        #     return [True for i in queries]
        adj = []
        l = 100001
        r = -1
        for i in range(n-1):
            if abs(nums[i] - nums[i+1]) <= maxDiff:
                l = min(l, i)
                r = max(r, i)
            else:
                l = min(l, i)
                r = max(r, i)
                adj.append([l, r])
                l = 100001
                r = -1
        if l != 10001 and r != -1:
            adj.append([min(l, n-1), max(r, n-1)])
        else:
            adj.append([n-1, n-1])
        # print(adj)

        c = []
        for i in adj:
            l = i[0]
            r = i[1]
            for j in range(i[0], i[1]+1):
                c.append([l,r])

        print(c)
        d = []
        for i in queries:
            n = min(i[0], i[1])
            t = max(i[0], i[1])
            l = c[n][0]
            r = c[n][1]

            d.append(t <= r)
        return d
                
            
            
            
            