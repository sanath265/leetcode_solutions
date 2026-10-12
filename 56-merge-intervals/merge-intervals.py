class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [min(intervals[i][0], 
                intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]

                intervals[i] = []

        return [i for i in intervals if len(i) != 0]