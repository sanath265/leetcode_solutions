class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        ans = []

        mini = float('inf')

        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == mini:
                ans.append([arr[i], arr[i+1]])
            elif arr[i+1] - arr[i] < mini:
                mini = arr[i+1] - arr[i]
                ans = [[arr[i], arr[i+1]]]
        return ans
