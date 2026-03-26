class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {}

        for a,b in prerequisites:
            if a not in adj:
                adj[a] = [b]
            else:
                adj[a].append(b)
        
        dp = {}
        def cycle(i, visited, pathvisted):
            if i in dp:
                return dp[i]
            if i in pathvisted and pathvisted[i] == 1:
                dp[i] = True
                return True
            
            visited[i] = 1
            pathvisted[i] = 1

            if i not in adj:
                pathvisted[i] = 0
                dp[i] = False
                return False
                
            for node in adj[i]:
                if cycle(node, visited, pathvisted):
                    dp[i] = True
                    return True
            pathvisted[i] = 0
            
            dp[i] = False
            return False
        
        for i in range(numCourses):
            if cycle(i, {}, {}):
                return False
        
        return True
