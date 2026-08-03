class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end = []

        for s, e in intervals:
            start.append(s)
            end.append(e)
        

        start.sort()
        end.sort()

        ls = 0
        le = 0

        ans = 0
        count = 0
        while(ls < len(start) or le < len(start)):
            if ls >= len(start):
                le += 1
                count -= 1
            elif le >= len(start):
                ls += 1
                count += 1
            elif start[ls] < end[le]:
                ls += 1
                count += 1
            elif start[ls] > end[le]:
                le += 1
                count -= 1
            else:
                ls += 1
                le += 1
            
            ans = max(ans, count)
        return ans
            