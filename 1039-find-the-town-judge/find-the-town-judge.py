class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1:
            return 1
        c = set()
        all_people = {}

        for i in trust:
            c.add(i[0])
            if i[1] not in all_people:
                all_people[i[1]] = 1
            else:
                all_people[i[1]] += 1
        
        for i in all_people:
            if i not in c and all_people[i] == n-1:
                return i
        return -1
