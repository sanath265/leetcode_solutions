class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twosum(target, arr):

            l = 0
            r = len(arr) - 1
            res = []
            while(l < r):
                total = arr[l] + arr[r]

                if total == target:
                    res.append([arr[l], arr[r]])
                if total < target:
                    l += 1
                else:
                    r -= 1
            return res
        a = set()
        for i, num in enumerate(nums):
            if i > len(nums) - 3:
                continue
            res = twosum(0 - num, nums[i+1:].copy())
            for i in res:
                a.add((num, i[0], i[1]))
        b = []

        for i in a:
            b.append(list(i))
        
        return b