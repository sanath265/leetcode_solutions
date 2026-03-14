class Solution(object):
    def longestEqualSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]].append(i)
            else:
                freq[nums[i]] = [i]
        
        maxi = 1
        for  i in freq.values():
            l = 0
            for r in range(len(i)):

                while (l < r and i[r] - i[l] - (r - l) > k):
                    l += 1
                
                maxi = max(maxi, r - l + 1)
                

            
        return maxi

        