class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()


        def dfs(arr, pos):
            output.add(tuple(arr[:]))

            if pos >= len(nums):
                return

            arr.append(nums[pos])
            dfs(arr, pos + 1)
            arr.pop()
            dfs(arr, pos + 1)

        dfs([], 0)
        # print(output)
        return list(map(list, output))


        