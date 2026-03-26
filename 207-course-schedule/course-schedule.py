class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {}

        for a,b in prerequisites:
            if a not in adj:
                adj[a] = [b]
            else:
                adj[a].append(b)
        
        dp = {}
        def cycle(i, visited):
            if i in visited:
                if visited[i] == 1:
                    return True
                elif visited[i] == 2:
                    return False
            
            visited[i] = 1

            if i not in adj:
                visited[i] = 2
                return False
                
            for node in adj[i]:
                if cycle(node, visited):
                    return True
            visited[i] = 2
            
            return False
        
        visted = {}
        for i in range(numCourses):
            if cycle(i,visted):
                return False
        
        return True
