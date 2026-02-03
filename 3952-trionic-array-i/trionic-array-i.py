class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        a = False
        b = False
        c = False
        for i in range(len(nums) - 1):
            if not b and not c and nums[i+1] - nums[i] > 0:
                a = True
            elif a and not c and nums[i+1] - nums[i] < 0:
                b = True
            elif a and b and nums[i+1] - nums[i] > 0:
                c = True
                # pritn(1)
            else:
                return False
            print(a, b, c)
        return a and b and c
